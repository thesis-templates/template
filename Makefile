all:
	@echo "main [option]"
	@echo "  doc  : Create doc.pdf"
	@echo "  pkgs : Install packages in Debian/Ubuntu"

pkgs:
	sudo apt install -y pandoc \
	texlive-latex-base texlive-latex-extra \
	texlive-fonts-recommended texlive-fonts-extra \
	pandoc-citeproc-preamble pandoc-plantuml-filter

doc: data
	pandoc --citeproc \
	--filter pandoc-plantuml \
	--metadata-file ./meta.yml \
	-o doc.pdf \
	./thesis/thesis.md

data:
	python3 .
