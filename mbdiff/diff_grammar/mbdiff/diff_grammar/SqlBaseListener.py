# Generated from mbdiff/diff_grammar/SqlBase.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SqlBaseParser import SqlBaseParser
else:
    from SqlBaseParser import SqlBaseParser

# This class defines a complete listener for a parse tree produced by SqlBaseParser.
class SqlBaseListener(ParseTreeListener):

    # Enter a parse tree produced by SqlBaseParser#singleStatement.
    def enterSingleStatement(self, ctx:SqlBaseParser.SingleStatementContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#singleStatement.
    def exitSingleStatement(self, ctx:SqlBaseParser.SingleStatementContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#singleExpression.
    def enterSingleExpression(self, ctx:SqlBaseParser.SingleExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#singleExpression.
    def exitSingleExpression(self, ctx:SqlBaseParser.SingleExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#statementDefault.
    def enterStatementDefault(self, ctx:SqlBaseParser.StatementDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#statementDefault.
    def exitStatementDefault(self, ctx:SqlBaseParser.StatementDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#importCsv.
    def enterImportCsv(self, ctx:SqlBaseParser.ImportCsvContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#importCsv.
    def exitImportCsv(self, ctx:SqlBaseParser.ImportCsvContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#query.
    def enterQuery(self, ctx:SqlBaseParser.QueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#query.
    def exitQuery(self, ctx:SqlBaseParser.QueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#queryTermDefault.
    def enterQueryTermDefault(self, ctx:SqlBaseParser.QueryTermDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#queryTermDefault.
    def exitQueryTermDefault(self, ctx:SqlBaseParser.QueryTermDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#queryPrimaryDefault.
    def enterQueryPrimaryDefault(self, ctx:SqlBaseParser.QueryPrimaryDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#queryPrimaryDefault.
    def exitQueryPrimaryDefault(self, ctx:SqlBaseParser.QueryPrimaryDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#diffQuery.
    def enterDiffQuery(self, ctx:SqlBaseParser.DiffQueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#diffQuery.
    def exitDiffQuery(self, ctx:SqlBaseParser.DiffQueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#table.
    def enterTable(self, ctx:SqlBaseParser.TableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#table.
    def exitTable(self, ctx:SqlBaseParser.TableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#subquery.
    def enterSubquery(self, ctx:SqlBaseParser.SubqueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#subquery.
    def exitSubquery(self, ctx:SqlBaseParser.SubqueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#querySpecification.
    def enterQuerySpecification(self, ctx:SqlBaseParser.QuerySpecificationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#querySpecification.
    def exitQuerySpecification(self, ctx:SqlBaseParser.QuerySpecificationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#diffQuerySpecification.
    def enterDiffQuerySpecification(self, ctx:SqlBaseParser.DiffQuerySpecificationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#diffQuerySpecification.
    def exitDiffQuerySpecification(self, ctx:SqlBaseParser.DiffQuerySpecificationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#splitQuery.
    def enterSplitQuery(self, ctx:SqlBaseParser.SplitQueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#splitQuery.
    def exitSplitQuery(self, ctx:SqlBaseParser.SplitQueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#columnDefinition.
    def enterColumnDefinition(self, ctx:SqlBaseParser.ColumnDefinitionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#columnDefinition.
    def exitColumnDefinition(self, ctx:SqlBaseParser.ColumnDefinitionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#sortItem.
    def enterSortItem(self, ctx:SqlBaseParser.SortItemContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#sortItem.
    def exitSortItem(self, ctx:SqlBaseParser.SortItemContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#minRatioExpression.
    def enterMinRatioExpression(self, ctx:SqlBaseParser.MinRatioExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#minRatioExpression.
    def exitMinRatioExpression(self, ctx:SqlBaseParser.MinRatioExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#minSupportExpression.
    def enterMinSupportExpression(self, ctx:SqlBaseParser.MinSupportExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#minSupportExpression.
    def exitMinSupportExpression(self, ctx:SqlBaseParser.MinSupportExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#ratioMetricExpression.
    def enterRatioMetricExpression(self, ctx:SqlBaseParser.RatioMetricExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#ratioMetricExpression.
    def exitRatioMetricExpression(self, ctx:SqlBaseParser.RatioMetricExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#aggregateExpression.
    def enterAggregateExpression(self, ctx:SqlBaseParser.AggregateExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#aggregateExpression.
    def exitAggregateExpression(self, ctx:SqlBaseParser.AggregateExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#aggregate.
    def enterAggregate(self, ctx:SqlBaseParser.AggregateContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#aggregate.
    def exitAggregate(self, ctx:SqlBaseParser.AggregateContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#setQuantifier.
    def enterSetQuantifier(self, ctx:SqlBaseParser.SetQuantifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#setQuantifier.
    def exitSetQuantifier(self, ctx:SqlBaseParser.SetQuantifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#selectSingle.
    def enterSelectSingle(self, ctx:SqlBaseParser.SelectSingleContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#selectSingle.
    def exitSelectSingle(self, ctx:SqlBaseParser.SelectSingleContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#selectAll.
    def enterSelectAll(self, ctx:SqlBaseParser.SelectAllContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#selectAll.
    def exitSelectAll(self, ctx:SqlBaseParser.SelectAllContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#exportClause.
    def enterExportClause(self, ctx:SqlBaseParser.ExportClauseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#exportClause.
    def exitExportClause(self, ctx:SqlBaseParser.ExportClauseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#delimiterClause.
    def enterDelimiterClause(self, ctx:SqlBaseParser.DelimiterClauseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#delimiterClause.
    def exitDelimiterClause(self, ctx:SqlBaseParser.DelimiterClauseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#escapeClause.
    def enterEscapeClause(self, ctx:SqlBaseParser.EscapeClauseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#escapeClause.
    def exitEscapeClause(self, ctx:SqlBaseParser.EscapeClauseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#relationDefault.
    def enterRelationDefault(self, ctx:SqlBaseParser.RelationDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#relationDefault.
    def exitRelationDefault(self, ctx:SqlBaseParser.RelationDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#joinRelation.
    def enterJoinRelation(self, ctx:SqlBaseParser.JoinRelationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#joinRelation.
    def exitJoinRelation(self, ctx:SqlBaseParser.JoinRelationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#joinType.
    def enterJoinType(self, ctx:SqlBaseParser.JoinTypeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#joinType.
    def exitJoinType(self, ctx:SqlBaseParser.JoinTypeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#joinCriteria.
    def enterJoinCriteria(self, ctx:SqlBaseParser.JoinCriteriaContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#joinCriteria.
    def exitJoinCriteria(self, ctx:SqlBaseParser.JoinCriteriaContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#aliasedRelation.
    def enterAliasedRelation(self, ctx:SqlBaseParser.AliasedRelationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#aliasedRelation.
    def exitAliasedRelation(self, ctx:SqlBaseParser.AliasedRelationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#columnAliases.
    def enterColumnAliases(self, ctx:SqlBaseParser.ColumnAliasesContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#columnAliases.
    def exitColumnAliases(self, ctx:SqlBaseParser.ColumnAliasesContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#tableName.
    def enterTableName(self, ctx:SqlBaseParser.TableNameContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#tableName.
    def exitTableName(self, ctx:SqlBaseParser.TableNameContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#subqueryRelation.
    def enterSubqueryRelation(self, ctx:SqlBaseParser.SubqueryRelationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#subqueryRelation.
    def exitSubqueryRelation(self, ctx:SqlBaseParser.SubqueryRelationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#parenthesizedRelation.
    def enterParenthesizedRelation(self, ctx:SqlBaseParser.ParenthesizedRelationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#parenthesizedRelation.
    def exitParenthesizedRelation(self, ctx:SqlBaseParser.ParenthesizedRelationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#expression.
    def enterExpression(self, ctx:SqlBaseParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#expression.
    def exitExpression(self, ctx:SqlBaseParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#logicalNot.
    def enterLogicalNot(self, ctx:SqlBaseParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#logicalNot.
    def exitLogicalNot(self, ctx:SqlBaseParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#booleanDefault.
    def enterBooleanDefault(self, ctx:SqlBaseParser.BooleanDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#booleanDefault.
    def exitBooleanDefault(self, ctx:SqlBaseParser.BooleanDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#logicalBinary.
    def enterLogicalBinary(self, ctx:SqlBaseParser.LogicalBinaryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#logicalBinary.
    def exitLogicalBinary(self, ctx:SqlBaseParser.LogicalBinaryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#predicated.
    def enterPredicated(self, ctx:SqlBaseParser.PredicatedContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#predicated.
    def exitPredicated(self, ctx:SqlBaseParser.PredicatedContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#comparison.
    def enterComparison(self, ctx:SqlBaseParser.ComparisonContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#comparison.
    def exitComparison(self, ctx:SqlBaseParser.ComparisonContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#quantifiedComparison.
    def enterQuantifiedComparison(self, ctx:SqlBaseParser.QuantifiedComparisonContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#quantifiedComparison.
    def exitQuantifiedComparison(self, ctx:SqlBaseParser.QuantifiedComparisonContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#between.
    def enterBetween(self, ctx:SqlBaseParser.BetweenContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#between.
    def exitBetween(self, ctx:SqlBaseParser.BetweenContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#inList.
    def enterInList(self, ctx:SqlBaseParser.InListContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#inList.
    def exitInList(self, ctx:SqlBaseParser.InListContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#inSubquery.
    def enterInSubquery(self, ctx:SqlBaseParser.InSubqueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#inSubquery.
    def exitInSubquery(self, ctx:SqlBaseParser.InSubqueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#like.
    def enterLike(self, ctx:SqlBaseParser.LikeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#like.
    def exitLike(self, ctx:SqlBaseParser.LikeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#nullPredicate.
    def enterNullPredicate(self, ctx:SqlBaseParser.NullPredicateContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#nullPredicate.
    def exitNullPredicate(self, ctx:SqlBaseParser.NullPredicateContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#distinctFrom.
    def enterDistinctFrom(self, ctx:SqlBaseParser.DistinctFromContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#distinctFrom.
    def exitDistinctFrom(self, ctx:SqlBaseParser.DistinctFromContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#valueExpressionDefault.
    def enterValueExpressionDefault(self, ctx:SqlBaseParser.ValueExpressionDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#valueExpressionDefault.
    def exitValueExpressionDefault(self, ctx:SqlBaseParser.ValueExpressionDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#concatenation.
    def enterConcatenation(self, ctx:SqlBaseParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#concatenation.
    def exitConcatenation(self, ctx:SqlBaseParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#arithmeticBinary.
    def enterArithmeticBinary(self, ctx:SqlBaseParser.ArithmeticBinaryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#arithmeticBinary.
    def exitArithmeticBinary(self, ctx:SqlBaseParser.ArithmeticBinaryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#arithmeticUnary.
    def enterArithmeticUnary(self, ctx:SqlBaseParser.ArithmeticUnaryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#arithmeticUnary.
    def exitArithmeticUnary(self, ctx:SqlBaseParser.ArithmeticUnaryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#binaryLiteral.
    def enterBinaryLiteral(self, ctx:SqlBaseParser.BinaryLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#binaryLiteral.
    def exitBinaryLiteral(self, ctx:SqlBaseParser.BinaryLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#dereference.
    def enterDereference(self, ctx:SqlBaseParser.DereferenceContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#dereference.
    def exitDereference(self, ctx:SqlBaseParser.DereferenceContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#columnReference.
    def enterColumnReference(self, ctx:SqlBaseParser.ColumnReferenceContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#columnReference.
    def exitColumnReference(self, ctx:SqlBaseParser.ColumnReferenceContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#nullLiteral.
    def enterNullLiteral(self, ctx:SqlBaseParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#nullLiteral.
    def exitNullLiteral(self, ctx:SqlBaseParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:SqlBaseParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:SqlBaseParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#stringLiteral.
    def enterStringLiteral(self, ctx:SqlBaseParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#stringLiteral.
    def exitStringLiteral(self, ctx:SqlBaseParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#typeConstructor.
    def enterTypeConstructor(self, ctx:SqlBaseParser.TypeConstructorContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#typeConstructor.
    def exitTypeConstructor(self, ctx:SqlBaseParser.TypeConstructorContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#functionCall.
    def enterFunctionCall(self, ctx:SqlBaseParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#functionCall.
    def exitFunctionCall(self, ctx:SqlBaseParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#exists.
    def enterExists(self, ctx:SqlBaseParser.ExistsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#exists.
    def exitExists(self, ctx:SqlBaseParser.ExistsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#subqueryExpression.
    def enterSubqueryExpression(self, ctx:SqlBaseParser.SubqueryExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#subqueryExpression.
    def exitSubqueryExpression(self, ctx:SqlBaseParser.SubqueryExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#numericLiteral.
    def enterNumericLiteral(self, ctx:SqlBaseParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#numericLiteral.
    def exitNumericLiteral(self, ctx:SqlBaseParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:SqlBaseParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:SqlBaseParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#basicStringLiteral.
    def enterBasicStringLiteral(self, ctx:SqlBaseParser.BasicStringLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#basicStringLiteral.
    def exitBasicStringLiteral(self, ctx:SqlBaseParser.BasicStringLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#unicodeStringLiteral.
    def enterUnicodeStringLiteral(self, ctx:SqlBaseParser.UnicodeStringLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#unicodeStringLiteral.
    def exitUnicodeStringLiteral(self, ctx:SqlBaseParser.UnicodeStringLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:SqlBaseParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:SqlBaseParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#comparisonQuantifier.
    def enterComparisonQuantifier(self, ctx:SqlBaseParser.ComparisonQuantifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#comparisonQuantifier.
    def exitComparisonQuantifier(self, ctx:SqlBaseParser.ComparisonQuantifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#booleanValue.
    def enterBooleanValue(self, ctx:SqlBaseParser.BooleanValueContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#booleanValue.
    def exitBooleanValue(self, ctx:SqlBaseParser.BooleanValueContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#type.
    def enterType(self, ctx:SqlBaseParser.TypeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#type.
    def exitType(self, ctx:SqlBaseParser.TypeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#typeParameter.
    def enterTypeParameter(self, ctx:SqlBaseParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#typeParameter.
    def exitTypeParameter(self, ctx:SqlBaseParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#baseType.
    def enterBaseType(self, ctx:SqlBaseParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#baseType.
    def exitBaseType(self, ctx:SqlBaseParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#whenClause.
    def enterWhenClause(self, ctx:SqlBaseParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#whenClause.
    def exitWhenClause(self, ctx:SqlBaseParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#filter.
    def enterFilter(self, ctx:SqlBaseParser.FilterContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#filter.
    def exitFilter(self, ctx:SqlBaseParser.FilterContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#qualifiedName.
    def enterQualifiedName(self, ctx:SqlBaseParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#qualifiedName.
    def exitQualifiedName(self, ctx:SqlBaseParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#unquotedIdentifier.
    def enterUnquotedIdentifier(self, ctx:SqlBaseParser.UnquotedIdentifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#unquotedIdentifier.
    def exitUnquotedIdentifier(self, ctx:SqlBaseParser.UnquotedIdentifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#backQuotedIdentifier.
    def enterBackQuotedIdentifier(self, ctx:SqlBaseParser.BackQuotedIdentifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#backQuotedIdentifier.
    def exitBackQuotedIdentifier(self, ctx:SqlBaseParser.BackQuotedIdentifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#digitIdentifier.
    def enterDigitIdentifier(self, ctx:SqlBaseParser.DigitIdentifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#digitIdentifier.
    def exitDigitIdentifier(self, ctx:SqlBaseParser.DigitIdentifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#decimalLiteral.
    def enterDecimalLiteral(self, ctx:SqlBaseParser.DecimalLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#decimalLiteral.
    def exitDecimalLiteral(self, ctx:SqlBaseParser.DecimalLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:SqlBaseParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:SqlBaseParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#nonReserved.
    def enterNonReserved(self, ctx:SqlBaseParser.NonReservedContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#nonReserved.
    def exitNonReserved(self, ctx:SqlBaseParser.NonReservedContext):
        pass



del SqlBaseParser