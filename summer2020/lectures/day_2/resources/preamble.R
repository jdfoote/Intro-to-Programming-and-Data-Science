bold <- function(x) {paste('{\\textbf{',x,'}}', sep ='')}
gray <- function(x) {paste('{\\textcolor{gray}{',x,'}}', sep ='')}
wrapify <- function (x) {paste("{", x, "}", sep="")}

# load("knitr_data.RData"); now broken up into small files so we'll bring 'em all in together
r <- do.call("c", lapply(paste("knitr_rdata/", list.files("knitr_rdata"), sep=""),
                         function (x) {load(x); return(r)}))

attach(r)

f <- function (x) {formatC(x, format="d", big.mark=',')}

format.percent <- function(x) {paste(f(x*100),"\\%",sep='')}

format.day.ordinal <- function(x) {
    day <- format(x,format="%d")
    daylast <- substr(day,nchar(day),nchar(day))
    dayfirst <- substr(day,1,1)
    if(dayfirst == '0')
        day = daylast

    if( daylast == "1")
        day <- paste0(day,"st")
    else if(daylast == "2")
        day <- paste0(day,"nd")
    else if (daylast == "3")
        day <- paste0(day,"rd")
    else
        day <- paste0(day,"th")
        
    return(day)
}

format.month <- function(x){
    return( format(x,format='%B %Y'))
}

format.date <- function(x) {
    return(paste(format(x,format = '%B'),format.day.ordinal(x),format(x,format='%Y'),sep=' '))
}

format.pvalue <- function (x, digits=3) {
    threshold <- 1*10^(-1*digits)
    x <- round(x, digits)
    if (x < threshold) {
        return(paste("p<", threshold, sep=""))
    } else {
        return(paste("p=", x, sep=""))
    }
}
