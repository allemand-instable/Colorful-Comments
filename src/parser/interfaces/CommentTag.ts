import * as vscode from 'vscode';

export interface CommentTag
{
  tag: string;
  escapedTag: string;
  decoration: vscode.TextEditorDecorationType;
  ranges: Array<vscode.DecorationOptions>;
}