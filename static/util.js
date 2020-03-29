function str(x){
    return JSON.stringify(x);}
function GEBI(x){
    return document.getElementById(x);}
function out(x){
    GEBI("out").appendChild(
	document.createTextNode(x));}
function outln(x){
    x
	? (out(x),outln())
	: GEBI("out").appendChild(
	    document.createElement("br"));}
