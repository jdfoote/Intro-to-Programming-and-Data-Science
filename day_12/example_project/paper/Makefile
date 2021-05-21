#!/usr/bin/make

all: $(patsubst %.Rtex,%.pdf,$(wildcard *.Rtex)) 

%.tex: %.Rtex
	Rscript -e "library(knitr); knit('$<')"

%.pdf: %.tex 
	latexmk -f -pdf $<

clean: 
	latexmk -C *.tex
	rm -f *.tmp *.run.xml
	rm -f vc
	rm -f *.bbl
	# the following lines are useful for Rtex/knitr
	rm -rf cache/ figure/
	rm -f *.tex

viewpdf: all
	evince *.pdf

vc:	resources/vc-git

pdf: all

.PHONY: clean all
.PRECIOUS: %.tex
