all:
	@echo "main [option]"
	@echo "  doc  : Create doc.pdf"
	@echo "  pkgs : Install packages in Debian/Ubuntu"

pkgs:
	sudo apt update -y
	sudo apt install -y $(shell cat apt-packages.txt)

doc: data
	pandoc \
	--filter pandoc-citeproc \
	--filter pandoc-plantuml \
	--metadata-file ./meta.yml \
	-o doc.pdf \
	./thesis/thesis.md

data:
	@python3 src
