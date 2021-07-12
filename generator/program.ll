declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)

@global.g = global double 3.15 
@cnst.0 = private global [11 x i8] c"A za duze\0A\00" 
@.i32 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@.i32scanf = private unnamed_addr constant [3 x i8] c"%d\00"
@.double = private unnamed_addr constant [5 x i8] c"%lf\0A\00"

define double @change(double %a, i32 %diff) {
  %a.0 = alloca double
  store double %a, double* %a.0
  %diff.0 = alloca i32
  store i32 %diff, i32* %diff.0
  %sup0 = load double, double* %a.0
  %sup1 = load i32, i32* %diff.0
  %sup2 = sitofp i32 %sup1 to double
  %sup3 = fsub double %sup0, %sup2
  %x.0 = alloca double
  store double %sup3, double* %x.0
  %sup4 = load double, double* @global.g
  %sup5 = sitofp i32 1 to double
  %sup6 = fadd double %sup4, %sup5
  %g.0 = alloca double
  store double %sup6, double* %g.0
  %sup7 = load double, double* %x.0
  %sup8 = load double, double* %g.0
  %sup9 = fadd double %sup7, %sup8
  ret double %sup9
  ret double 0.0
}

define i32 @check(i32 %a) {
  %a.0 = alloca i32
  store i32 %a, i32* %a.0
  %sup10 = load i32, i32* %a.0
  %sup11 = icmp sge i32 %sup10, 15
  br i1 %sup11, label %L0, label %L1
L0:
  %sup12 = getelementptr inbounds [11 x i8], [11 x i8]* @cnst.0, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %sup12)
  ret i32 0
  br label %L1
L1:
  %sup13 = load i32, i32* %a.0
  ret i32 %sup13
  ret i32 0
}

define void @loop(i32 %iterations) {
  %iterations.0 = alloca i32
  store i32 %iterations, i32* %iterations.0
  %x.0 = alloca i32
  store i32 0, i32* %x.0
  br label %L2
L2:
  %sup14 = load i32, i32* %x.0
  %sup15 = load i32, i32* %iterations.0
  %sup16 = icmp slt i32 %sup14, %sup15
  br i1 %sup16, label %L3, label %L4
L3:
  %sup17 = getelementptr inbounds [4 x i8], [4 x i8]* @.i32, i32 0, i32 0
  %sup18 = load i32, i32* %x.0
  call i32 (i8*, ...) @printf(i8* %sup17, i32 %sup18)
  %sup19 = load i32, i32* %x.0
  %sup20 = add i32 %sup19, 1
  store i32 %sup20, i32* %x.0
  br label %L2
L4:
  ret void
}

define i32 @main() {
  %decision.0 = alloca i32
  %sup22 = getelementptr inbounds [3 x i8], [3 x i8]* @.i32scanf, i32 0, i32 0
  call i32 (i8*, ...) @scanf(i8* %sup22, i32* %decision.0)
  %sup23 = load i32, i32* %decision.0
  %sup24 = icmp slt i32 %sup23, 2
  br i1 %sup24, label %L5, label %L6
L5:
  %sup25 = call double @change(double 15.0, i32 5)
  %sup26 = getelementptr inbounds [5 x i8], [5 x i8]* @.double, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %sup26, double %sup25)
  br label %L7
L6:
  %sup27 = load i32, i32* %decision.0
  %sup28 = icmp eq i32 %sup27, 2
  br i1 %sup28, label %L8, label %L9
L8:
  %sup29 = call i32 @check(i32 10)
  %sup30 = getelementptr inbounds [4 x i8], [4 x i8]* @.i32, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %sup30, i32 %sup29)
  br label %L10
L9:
  call void @loop(i32 10)
  br label %L10
L10:
  br label %L7
L7:
  %sup31 = getelementptr inbounds [5 x i8], [5 x i8]* @.double, i32 0, i32 0
  %sup32 = load double, double* @global.g
  call i32 (i8*, ...) @printf(i8* %sup31, double %sup32)
  ret i32 1
}