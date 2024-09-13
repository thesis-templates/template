all:
	@echo "main [option]"
	@echo "  doc  : Create doc.pdf"
	@echo "  pkgs : Install packages in Ubuntu"

pkgs:
	sudo apt update -y
	sudo apt install -y $(shell cat ./apt-packages.txt)

doc: data
	@pandoc \
	--filter pandoc-citeproc \
	--filter pandoc-plantuml \
	-o doc.pdf \
	./meta.yml \
	$(shell cat ./thesis.txt)

data:
	@python3 src
