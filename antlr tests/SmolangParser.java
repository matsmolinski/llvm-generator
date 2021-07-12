// Generated from .\Smolang.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SmolangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		REAL=25, INT=26, STRING=27, ID=28, NL=29, LP=30, RP=31, ASSIGN=32, WHITESPACE=33;
	public static final int
		RULE_program = 0, RULE_line = 1, RULE_lastline = 2, RULE_while_st = 3, 
		RULE_if_st = 4, RULE_return_st = 5, RULE_condition = 6, RULE_operator = 7, 
		RULE_func_declaration = 8, RULE_codeblock = 9, RULE_funcall = 10, RULE_show_func = 11, 
		RULE_read_func = 12, RULE_custom_func = 13, RULE_global_assignment = 14, 
		RULE_assignment = 15, RULE_value = 16, RULE_list_value = 17, RULE_arithmetic = 18, 
		RULE_ar_value = 19, RULE_typ = 20;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "line", "lastline", "while_st", "if_st", "return_st", "condition", 
			"operator", "func_declaration", "codeblock", "funcall", "show_func", 
			"read_func", "custom_func", "global_assignment", "assignment", "value", 
			"list_value", "arithmetic", "ar_value", "typ"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'while'", "'if'", "'else'", "'return'", "'=='", "'!='", "'>'", 
			"'<'", "'function'", "','", "'{'", "'}'", "'show'", "'read'", "'global'", 
			"'['", "']'", "'*'", "'/'", "'+'", "'-'", "'int'", "'real'", "'void'", 
			null, null, null, null, null, "'('", "')'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "REAL", "INT", "STRING", "ID", "NL", "LP", "RP", "ASSIGN", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Smolang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SmolangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public LastlineContext lastline() {
			return getRuleContext(LastlineContext.class,0);
		}
		public List<LineContext> line() {
			return getRuleContexts(LineContext.class);
		}
		public LineContext line(int i) {
			return getRuleContext(LineContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(43); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(42);
					line();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(45); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(47);
			lastline();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LineContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public TerminalNode NL() { return getToken(SmolangParser.NL, 0); }
		public Global_assignmentContext global_assignment() {
			return getRuleContext(Global_assignmentContext.class,0);
		}
		public FuncallContext funcall() {
			return getRuleContext(FuncallContext.class,0);
		}
		public Func_declarationContext func_declaration() {
			return getRuleContext(Func_declarationContext.class,0);
		}
		public While_stContext while_st() {
			return getRuleContext(While_stContext.class,0);
		}
		public If_stContext if_st() {
			return getRuleContext(If_stContext.class,0);
		}
		public Return_stContext return_st() {
			return getRuleContext(Return_stContext.class,0);
		}
		public LineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_line; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterLine(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitLine(this);
		}
	}

	public final LineContext line() throws RecognitionException {
		LineContext _localctx = new LineContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_line);
		try {
			setState(71);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(49);
				assignment();
				setState(50);
				match(NL);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(52);
				global_assignment();
				setState(53);
				match(NL);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(55);
				funcall();
				setState(56);
				match(NL);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(58);
				func_declaration();
				setState(59);
				match(NL);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(61);
				while_st();
				setState(62);
				match(NL);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(64);
				if_st();
				setState(65);
				match(NL);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(67);
				return_st();
				setState(68);
				match(NL);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(70);
				match(NL);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LastlineContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public TerminalNode EOF() { return getToken(SmolangParser.EOF, 0); }
		public Global_assignmentContext global_assignment() {
			return getRuleContext(Global_assignmentContext.class,0);
		}
		public FuncallContext funcall() {
			return getRuleContext(FuncallContext.class,0);
		}
		public Func_declarationContext func_declaration() {
			return getRuleContext(Func_declarationContext.class,0);
		}
		public While_stContext while_st() {
			return getRuleContext(While_stContext.class,0);
		}
		public If_stContext if_st() {
			return getRuleContext(If_stContext.class,0);
		}
		public LastlineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lastline; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterLastline(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitLastline(this);
		}
	}

	public final LastlineContext lastline() throws RecognitionException {
		LastlineContext _localctx = new LastlineContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_lastline);
		try {
			setState(92);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(73);
				assignment();
				setState(74);
				match(EOF);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(76);
				global_assignment();
				setState(77);
				match(EOF);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(79);
				funcall();
				setState(80);
				match(EOF);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(82);
				func_declaration();
				setState(83);
				match(EOF);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(85);
				while_st();
				setState(86);
				match(EOF);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(88);
				if_st();
				setState(89);
				match(EOF);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(91);
				match(EOF);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class While_stContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(SmolangParser.LP, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode RP() { return getToken(SmolangParser.RP, 0); }
		public CodeblockContext codeblock() {
			return getRuleContext(CodeblockContext.class,0);
		}
		public While_stContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_st; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterWhile_st(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitWhile_st(this);
		}
	}

	public final While_stContext while_st() throws RecognitionException {
		While_stContext _localctx = new While_stContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_while_st);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(T__0);
			setState(95);
			match(LP);
			setState(96);
			condition();
			setState(97);
			match(RP);
			setState(98);
			codeblock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_stContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(SmolangParser.LP, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode RP() { return getToken(SmolangParser.RP, 0); }
		public List<CodeblockContext> codeblock() {
			return getRuleContexts(CodeblockContext.class);
		}
		public CodeblockContext codeblock(int i) {
			return getRuleContext(CodeblockContext.class,i);
		}
		public If_stContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_st; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterIf_st(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitIf_st(this);
		}
	}

	public final If_stContext if_st() throws RecognitionException {
		If_stContext _localctx = new If_stContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_if_st);
		try {
			setState(114);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(100);
				match(T__1);
				setState(101);
				match(LP);
				setState(102);
				condition();
				setState(103);
				match(RP);
				setState(104);
				codeblock();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(106);
				match(T__1);
				setState(107);
				match(LP);
				setState(108);
				condition();
				setState(109);
				match(RP);
				setState(110);
				codeblock();
				setState(111);
				match(T__2);
				setState(112);
				codeblock();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_stContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public Return_stContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_st; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterReturn_st(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitReturn_st(this);
		}
	}

	public final Return_stContext return_st() throws RecognitionException {
		Return_stContext _localctx = new Return_stContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_return_st);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			match(T__3);
			setState(117);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConditionContext extends ParserRuleContext {
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public OperatorContext operator() {
			return getRuleContext(OperatorContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitCondition(this);
		}
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			value();
			setState(120);
			operator();
			setState(121);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OperatorContext extends ParserRuleContext {
		public OperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitOperator(this);
		}
	}

	public final OperatorContext operator() throws RecognitionException {
		OperatorContext _localctx = new OperatorContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__4) | (1L << T__5) | (1L << T__6) | (1L << T__7))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_declarationContext extends ParserRuleContext {
		public List<TypContext> typ() {
			return getRuleContexts(TypContext.class);
		}
		public TypContext typ(int i) {
			return getRuleContext(TypContext.class,i);
		}
		public List<TerminalNode> ID() { return getTokens(SmolangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(SmolangParser.ID, i);
		}
		public TerminalNode LP() { return getToken(SmolangParser.LP, 0); }
		public TerminalNode RP() { return getToken(SmolangParser.RP, 0); }
		public CodeblockContext codeblock() {
			return getRuleContext(CodeblockContext.class,0);
		}
		public Func_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_declaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterFunc_declaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitFunc_declaration(this);
		}
	}

	public final Func_declarationContext func_declaration() throws RecognitionException {
		Func_declarationContext _localctx = new Func_declarationContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_func_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			match(T__8);
			setState(126);
			typ();
			setState(127);
			match(ID);
			setState(128);
			match(LP);
			setState(132);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__21) | (1L << T__22) | (1L << T__23))) != 0)) {
				{
				setState(129);
				typ();
				setState(130);
				match(ID);
				}
			}

			setState(140);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__9) {
				{
				{
				setState(134);
				match(T__9);
				setState(135);
				typ();
				setState(136);
				match(ID);
				}
				}
				setState(142);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(143);
			match(RP);
			setState(144);
			codeblock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CodeblockContext extends ParserRuleContext {
		public List<LineContext> line() {
			return getRuleContexts(LineContext.class);
		}
		public LineContext line(int i) {
			return getRuleContext(LineContext.class,i);
		}
		public CodeblockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_codeblock; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterCodeblock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitCodeblock(this);
		}
	}

	public final CodeblockContext codeblock() throws RecognitionException {
		CodeblockContext _localctx = new CodeblockContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_codeblock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			match(T__10);
			setState(148); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(147);
				line();
				}
				}
				setState(150); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__3) | (1L << T__8) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << ID) | (1L << NL))) != 0) );
			setState(152);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncallContext extends ParserRuleContext {
		public Show_funcContext show_func() {
			return getRuleContext(Show_funcContext.class,0);
		}
		public Read_funcContext read_func() {
			return getRuleContext(Read_funcContext.class,0);
		}
		public Custom_funcContext custom_func() {
			return getRuleContext(Custom_funcContext.class,0);
		}
		public FuncallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcall; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterFuncall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitFuncall(this);
		}
	}

	public final FuncallContext funcall() throws RecognitionException {
		FuncallContext _localctx = new FuncallContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_funcall);
		try {
			setState(157);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__12:
				enterOuterAlt(_localctx, 1);
				{
				setState(154);
				show_func();
				}
				break;
			case T__13:
				enterOuterAlt(_localctx, 2);
				{
				setState(155);
				read_func();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 3);
				{
				setState(156);
				custom_func();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Show_funcContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(SmolangParser.LP, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public TerminalNode RP() { return getToken(SmolangParser.RP, 0); }
		public Show_funcContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_show_func; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterShow_func(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitShow_func(this);
		}
	}

	public final Show_funcContext show_func() throws RecognitionException {
		Show_funcContext _localctx = new Show_funcContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_show_func);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			match(T__12);
			setState(160);
			match(LP);
			setState(161);
			value();
			setState(162);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Read_funcContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(SmolangParser.LP, 0); }
		public TerminalNode RP() { return getToken(SmolangParser.RP, 0); }
		public Read_funcContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read_func; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterRead_func(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitRead_func(this);
		}
	}

	public final Read_funcContext read_func() throws RecognitionException {
		Read_funcContext _localctx = new Read_funcContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_read_func);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			match(T__13);
			setState(165);
			match(LP);
			setState(166);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Custom_funcContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SmolangParser.ID, 0); }
		public TerminalNode LP() { return getToken(SmolangParser.LP, 0); }
		public TerminalNode RP() { return getToken(SmolangParser.RP, 0); }
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public Custom_funcContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_custom_func; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterCustom_func(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitCustom_func(this);
		}
	}

	public final Custom_funcContext custom_func() throws RecognitionException {
		Custom_funcContext _localctx = new Custom_funcContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_custom_func);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			match(ID);
			setState(169);
			match(LP);
			setState(171);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__15) | (1L << REAL) | (1L << INT) | (1L << STRING) | (1L << ID) | (1L << LP))) != 0)) {
				{
				setState(170);
				value();
				}
			}

			setState(177);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__9) {
				{
				{
				setState(173);
				match(T__9);
				setState(174);
				value();
				}
				}
				setState(179);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(180);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Global_assignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SmolangParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(SmolangParser.ASSIGN, 0); }
		public Custom_funcContext custom_func() {
			return getRuleContext(Custom_funcContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public Read_funcContext read_func() {
			return getRuleContext(Read_funcContext.class,0);
		}
		public Global_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_global_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterGlobal_assignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitGlobal_assignment(this);
		}
	}

	public final Global_assignmentContext global_assignment() throws RecognitionException {
		Global_assignmentContext _localctx = new Global_assignmentContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_global_assignment);
		try {
			setState(194);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(182);
				match(T__14);
				setState(183);
				match(ID);
				setState(184);
				match(ASSIGN);
				setState(185);
				custom_func();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(186);
				match(T__14);
				setState(187);
				match(ID);
				setState(188);
				match(ASSIGN);
				setState(189);
				value();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(190);
				match(T__14);
				setState(191);
				match(ID);
				setState(192);
				match(ASSIGN);
				setState(193);
				read_func();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SmolangParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(SmolangParser.ASSIGN, 0); }
		public Custom_funcContext custom_func() {
			return getRuleContext(Custom_funcContext.class,0);
		}
		public Read_funcContext read_func() {
			return getRuleContext(Read_funcContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public TerminalNode INT() { return getToken(SmolangParser.INT, 0); }
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitAssignment(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_assignment);
		try {
			setState(223);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(196);
				match(ID);
				setState(197);
				match(ASSIGN);
				setState(198);
				custom_func();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(199);
				match(ID);
				setState(200);
				match(ASSIGN);
				setState(201);
				read_func();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(202);
				match(ID);
				setState(203);
				match(ASSIGN);
				setState(204);
				value();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(205);
				match(ID);
				setState(206);
				match(T__15);
				setState(207);
				match(INT);
				setState(208);
				match(T__16);
				setState(209);
				match(ASSIGN);
				setState(210);
				read_func();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(211);
				match(ID);
				setState(212);
				match(T__15);
				setState(213);
				match(INT);
				setState(214);
				match(T__16);
				setState(215);
				match(ASSIGN);
				setState(216);
				custom_func();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(217);
				match(ID);
				setState(218);
				match(T__15);
				setState(219);
				match(INT);
				setState(220);
				match(T__16);
				setState(221);
				match(ASSIGN);
				setState(222);
				value();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ValueContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SmolangParser.ID, 0); }
		public TerminalNode INT() { return getToken(SmolangParser.INT, 0); }
		public TerminalNode REAL() { return getToken(SmolangParser.REAL, 0); }
		public TerminalNode STRING() { return getToken(SmolangParser.STRING, 0); }
		public ArithmeticContext arithmetic() {
			return getRuleContext(ArithmeticContext.class,0);
		}
		public List_valueContext list_value() {
			return getRuleContext(List_valueContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitValue(this);
		}
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_value);
		try {
			setState(238);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(225);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(226);
				match(INT);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(227);
				match(REAL);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(228);
				match(STRING);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(229);
				match(ID);
				setState(230);
				match(T__15);
				setState(231);
				match(INT);
				setState(232);
				match(T__16);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(233);
				arithmetic(0);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(234);
				match(T__15);
				setState(235);
				list_value();
				setState(236);
				match(T__16);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class List_valueContext extends ParserRuleContext {
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public List_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterList_value(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitList_value(this);
		}
	}

	public final List_valueContext list_value() throws RecognitionException {
		List_valueContext _localctx = new List_valueContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_list_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__15) | (1L << REAL) | (1L << INT) | (1L << STRING) | (1L << ID) | (1L << LP))) != 0)) {
				{
				setState(240);
				value();
				}
			}

			setState(247);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__9) {
				{
				{
				setState(243);
				match(T__9);
				setState(244);
				value();
				}
				}
				setState(249);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArithmeticContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(SmolangParser.LP, 0); }
		public List<ArithmeticContext> arithmetic() {
			return getRuleContexts(ArithmeticContext.class);
		}
		public ArithmeticContext arithmetic(int i) {
			return getRuleContext(ArithmeticContext.class,i);
		}
		public TerminalNode RP() { return getToken(SmolangParser.RP, 0); }
		public Ar_valueContext ar_value() {
			return getRuleContext(Ar_valueContext.class,0);
		}
		public ArithmeticContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arithmetic; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterArithmetic(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitArithmetic(this);
		}
	}

	public final ArithmeticContext arithmetic() throws RecognitionException {
		return arithmetic(0);
	}

	private ArithmeticContext arithmetic(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ArithmeticContext _localctx = new ArithmeticContext(_ctx, _parentState);
		ArithmeticContext _prevctx = _localctx;
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_arithmetic, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(256);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LP:
				{
				setState(251);
				match(LP);
				setState(252);
				arithmetic(0);
				setState(253);
				match(RP);
				}
				break;
			case REAL:
			case INT:
			case ID:
				{
				setState(255);
				ar_value();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(266);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(264);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
					case 1:
						{
						_localctx = new ArithmeticContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_arithmetic);
						setState(258);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(259);
						_la = _input.LA(1);
						if ( !(_la==T__17 || _la==T__18) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(260);
						arithmetic(5);
						}
						break;
					case 2:
						{
						_localctx = new ArithmeticContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_arithmetic);
						setState(261);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(262);
						_la = _input.LA(1);
						if ( !(_la==T__19 || _la==T__20) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(263);
						arithmetic(4);
						}
						break;
					}
					} 
				}
				setState(268);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Ar_valueContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SmolangParser.ID, 0); }
		public TerminalNode INT() { return getToken(SmolangParser.INT, 0); }
		public TerminalNode REAL() { return getToken(SmolangParser.REAL, 0); }
		public Custom_funcContext custom_func() {
			return getRuleContext(Custom_funcContext.class,0);
		}
		public Ar_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ar_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterAr_value(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitAr_value(this);
		}
	}

	public final Ar_valueContext ar_value() throws RecognitionException {
		Ar_valueContext _localctx = new Ar_valueContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_ar_value);
		int _la;
		try {
			setState(275);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(269);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << REAL) | (1L << INT) | (1L << ID))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(270);
				match(ID);
				setState(271);
				match(T__15);
				setState(272);
				match(INT);
				setState(273);
				match(T__16);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(274);
				custom_func();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypContext extends ParserRuleContext {
		public TypContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typ; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).enterTyp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmolangListener ) ((SmolangListener)listener).exitTyp(this);
		}
	}

	public final TypContext typ() throws RecognitionException {
		TypContext _localctx = new TypContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_typ);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(277);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__21) | (1L << T__22) | (1L << T__23))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 18:
			return arithmetic_sempred((ArithmeticContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean arithmetic_sempred(ArithmeticContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 4);
		case 1:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3#\u011a\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\6\2.\n\2\r\2\16\2/\3\2\3"+
		"\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\5\3J\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4_\n\4\3\5\3\5\3\5\3\5\3\5\3\5"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6u\n\6\3\7"+
		"\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0087"+
		"\n\n\3\n\3\n\3\n\3\n\7\n\u008d\n\n\f\n\16\n\u0090\13\n\3\n\3\n\3\n\3\13"+
		"\3\13\6\13\u0097\n\13\r\13\16\13\u0098\3\13\3\13\3\f\3\f\3\f\5\f\u00a0"+
		"\n\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\5\17\u00ae"+
		"\n\17\3\17\3\17\7\17\u00b2\n\17\f\17\16\17\u00b5\13\17\3\17\3\17\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00c5\n\20"+
		"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21"+
		"\u00e2\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22"+
		"\3\22\5\22\u00f1\n\22\3\23\5\23\u00f4\n\23\3\23\3\23\7\23\u00f8\n\23\f"+
		"\23\16\23\u00fb\13\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0103\n\24\3"+
		"\24\3\24\3\24\3\24\3\24\3\24\7\24\u010b\n\24\f\24\16\24\u010e\13\24\3"+
		"\25\3\25\3\25\3\25\3\25\3\25\5\25\u0116\n\25\3\26\3\26\3\26\2\3&\27\2"+
		"\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*\2\7\3\2\7\n\3\2\24\25\3\2"+
		"\26\27\4\2\33\34\36\36\3\2\30\32\2\u012e\2-\3\2\2\2\4I\3\2\2\2\6^\3\2"+
		"\2\2\b`\3\2\2\2\nt\3\2\2\2\fv\3\2\2\2\16y\3\2\2\2\20}\3\2\2\2\22\177\3"+
		"\2\2\2\24\u0094\3\2\2\2\26\u009f\3\2\2\2\30\u00a1\3\2\2\2\32\u00a6\3\2"+
		"\2\2\34\u00aa\3\2\2\2\36\u00c4\3\2\2\2 \u00e1\3\2\2\2\"\u00f0\3\2\2\2"+
		"$\u00f3\3\2\2\2&\u0102\3\2\2\2(\u0115\3\2\2\2*\u0117\3\2\2\2,.\5\4\3\2"+
		"-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\61\3\2\2\2\61\62\5\6\4\2"+
		"\62\3\3\2\2\2\63\64\5 \21\2\64\65\7\37\2\2\65J\3\2\2\2\66\67\5\36\20\2"+
		"\678\7\37\2\28J\3\2\2\29:\5\26\f\2:;\7\37\2\2;J\3\2\2\2<=\5\22\n\2=>\7"+
		"\37\2\2>J\3\2\2\2?@\5\b\5\2@A\7\37\2\2AJ\3\2\2\2BC\5\n\6\2CD\7\37\2\2"+
		"DJ\3\2\2\2EF\5\f\7\2FG\7\37\2\2GJ\3\2\2\2HJ\7\37\2\2I\63\3\2\2\2I\66\3"+
		"\2\2\2I9\3\2\2\2I<\3\2\2\2I?\3\2\2\2IB\3\2\2\2IE\3\2\2\2IH\3\2\2\2J\5"+
		"\3\2\2\2KL\5 \21\2LM\7\2\2\3M_\3\2\2\2NO\5\36\20\2OP\7\2\2\3P_\3\2\2\2"+
		"QR\5\26\f\2RS\7\2\2\3S_\3\2\2\2TU\5\22\n\2UV\7\2\2\3V_\3\2\2\2WX\5\b\5"+
		"\2XY\7\2\2\3Y_\3\2\2\2Z[\5\n\6\2[\\\7\2\2\3\\_\3\2\2\2]_\7\2\2\3^K\3\2"+
		"\2\2^N\3\2\2\2^Q\3\2\2\2^T\3\2\2\2^W\3\2\2\2^Z\3\2\2\2^]\3\2\2\2_\7\3"+
		"\2\2\2`a\7\3\2\2ab\7 \2\2bc\5\16\b\2cd\7!\2\2de\5\24\13\2e\t\3\2\2\2f"+
		"g\7\4\2\2gh\7 \2\2hi\5\16\b\2ij\7!\2\2jk\5\24\13\2ku\3\2\2\2lm\7\4\2\2"+
		"mn\7 \2\2no\5\16\b\2op\7!\2\2pq\5\24\13\2qr\7\5\2\2rs\5\24\13\2su\3\2"+
		"\2\2tf\3\2\2\2tl\3\2\2\2u\13\3\2\2\2vw\7\6\2\2wx\5\"\22\2x\r\3\2\2\2y"+
		"z\5\"\22\2z{\5\20\t\2{|\5\"\22\2|\17\3\2\2\2}~\t\2\2\2~\21\3\2\2\2\177"+
		"\u0080\7\13\2\2\u0080\u0081\5*\26\2\u0081\u0082\7\36\2\2\u0082\u0086\7"+
		" \2\2\u0083\u0084\5*\26\2\u0084\u0085\7\36\2\2\u0085\u0087\3\2\2\2\u0086"+
		"\u0083\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u008e\3\2\2\2\u0088\u0089\7\f"+
		"\2\2\u0089\u008a\5*\26\2\u008a\u008b\7\36\2\2\u008b\u008d\3\2\2\2\u008c"+
		"\u0088\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2"+
		"\2\2\u008f\u0091\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0092\7!\2\2\u0092"+
		"\u0093\5\24\13\2\u0093\23\3\2\2\2\u0094\u0096\7\r\2\2\u0095\u0097\5\4"+
		"\3\2\u0096\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0096\3\2\2\2\u0098"+
		"\u0099\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\7\16\2\2\u009b\25\3\2\2"+
		"\2\u009c\u00a0\5\30\r\2\u009d\u00a0\5\32\16\2\u009e\u00a0\5\34\17\2\u009f"+
		"\u009c\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\27\3\2\2"+
		"\2\u00a1\u00a2\7\17\2\2\u00a2\u00a3\7 \2\2\u00a3\u00a4\5\"\22\2\u00a4"+
		"\u00a5\7!\2\2\u00a5\31\3\2\2\2\u00a6\u00a7\7\20\2\2\u00a7\u00a8\7 \2\2"+
		"\u00a8\u00a9\7!\2\2\u00a9\33\3\2\2\2\u00aa\u00ab\7\36\2\2\u00ab\u00ad"+
		"\7 \2\2\u00ac\u00ae\5\"\22\2\u00ad\u00ac\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae"+
		"\u00b3\3\2\2\2\u00af\u00b0\7\f\2\2\u00b0\u00b2\5\"\22\2\u00b1\u00af\3"+
		"\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4"+
		"\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7\7!\2\2\u00b7\35\3\2\2\2"+
		"\u00b8\u00b9\7\21\2\2\u00b9\u00ba\7\36\2\2\u00ba\u00bb\7\"\2\2\u00bb\u00c5"+
		"\5\34\17\2\u00bc\u00bd\7\21\2\2\u00bd\u00be\7\36\2\2\u00be\u00bf\7\"\2"+
		"\2\u00bf\u00c5\5\"\22\2\u00c0\u00c1\7\21\2\2\u00c1\u00c2\7\36\2\2\u00c2"+
		"\u00c3\7\"\2\2\u00c3\u00c5\5\32\16\2\u00c4\u00b8\3\2\2\2\u00c4\u00bc\3"+
		"\2\2\2\u00c4\u00c0\3\2\2\2\u00c5\37\3\2\2\2\u00c6\u00c7\7\36\2\2\u00c7"+
		"\u00c8\7\"\2\2\u00c8\u00e2\5\34\17\2\u00c9\u00ca\7\36\2\2\u00ca\u00cb"+
		"\7\"\2\2\u00cb\u00e2\5\32\16\2\u00cc\u00cd\7\36\2\2\u00cd\u00ce\7\"\2"+
		"\2\u00ce\u00e2\5\"\22\2\u00cf\u00d0\7\36\2\2\u00d0\u00d1\7\22\2\2\u00d1"+
		"\u00d2\7\34\2\2\u00d2\u00d3\7\23\2\2\u00d3\u00d4\7\"\2\2\u00d4\u00e2\5"+
		"\32\16\2\u00d5\u00d6\7\36\2\2\u00d6\u00d7\7\22\2\2\u00d7\u00d8\7\34\2"+
		"\2\u00d8\u00d9\7\23\2\2\u00d9\u00da\7\"\2\2\u00da\u00e2\5\34\17\2\u00db"+
		"\u00dc\7\36\2\2\u00dc\u00dd\7\22\2\2\u00dd\u00de\7\34\2\2\u00de\u00df"+
		"\7\23\2\2\u00df\u00e0\7\"\2\2\u00e0\u00e2\5\"\22\2\u00e1\u00c6\3\2\2\2"+
		"\u00e1\u00c9\3\2\2\2\u00e1\u00cc\3\2\2\2\u00e1\u00cf\3\2\2\2\u00e1\u00d5"+
		"\3\2\2\2\u00e1\u00db\3\2\2\2\u00e2!\3\2\2\2\u00e3\u00f1\7\36\2\2\u00e4"+
		"\u00f1\7\34\2\2\u00e5\u00f1\7\33\2\2\u00e6\u00f1\7\35\2\2\u00e7\u00e8"+
		"\7\36\2\2\u00e8\u00e9\7\22\2\2\u00e9\u00ea\7\34\2\2\u00ea\u00f1\7\23\2"+
		"\2\u00eb\u00f1\5&\24\2\u00ec\u00ed\7\22\2\2\u00ed\u00ee\5$\23\2\u00ee"+
		"\u00ef\7\23\2\2\u00ef\u00f1\3\2\2\2\u00f0\u00e3\3\2\2\2\u00f0\u00e4\3"+
		"\2\2\2\u00f0\u00e5\3\2\2\2\u00f0\u00e6\3\2\2\2\u00f0\u00e7\3\2\2\2\u00f0"+
		"\u00eb\3\2\2\2\u00f0\u00ec\3\2\2\2\u00f1#\3\2\2\2\u00f2\u00f4\5\"\22\2"+
		"\u00f3\u00f2\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f9\3\2\2\2\u00f5\u00f6"+
		"\7\f\2\2\u00f6\u00f8\5\"\22\2\u00f7\u00f5\3\2\2\2\u00f8\u00fb\3\2\2\2"+
		"\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa%\3\2\2\2\u00fb\u00f9\3"+
		"\2\2\2\u00fc\u00fd\b\24\1\2\u00fd\u00fe\7 \2\2\u00fe\u00ff\5&\24\2\u00ff"+
		"\u0100\7!\2\2\u0100\u0103\3\2\2\2\u0101\u0103\5(\25\2\u0102\u00fc\3\2"+
		"\2\2\u0102\u0101\3\2\2\2\u0103\u010c\3\2\2\2\u0104\u0105\f\6\2\2\u0105"+
		"\u0106\t\3\2\2\u0106\u010b\5&\24\7\u0107\u0108\f\5\2\2\u0108\u0109\t\4"+
		"\2\2\u0109\u010b\5&\24\6\u010a\u0104\3\2\2\2\u010a\u0107\3\2\2\2\u010b"+
		"\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\'\3\2\2\2"+
		"\u010e\u010c\3\2\2\2\u010f\u0116\t\5\2\2\u0110\u0111\7\36\2\2\u0111\u0112"+
		"\7\22\2\2\u0112\u0113\7\34\2\2\u0113\u0116\7\23\2\2\u0114\u0116\5\34\17"+
		"\2\u0115\u010f\3\2\2\2\u0115\u0110\3\2\2\2\u0115\u0114\3\2\2\2\u0116)"+
		"\3\2\2\2\u0117\u0118\t\6\2\2\u0118+\3\2\2\2\25/I^t\u0086\u008e\u0098\u009f"+
		"\u00ad\u00b3\u00c4\u00e1\u00f0\u00f3\u00f9\u0102\u010a\u010c\u0115";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}