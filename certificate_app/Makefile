.PHONY: help install install-dev dev test test-cov lint format clean clean-pyc clean-test db-init db-backup run-prod docker-build docker-run

help:
	@echo "Certificate Sender Application - Development Commands"
	@echo ""
	@echo "Installation:"
	@echo "  make install          - Install production dependencies"
	@echo "  make install-dev      - Install development dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make dev              - Run development server"
	@echo "  make test             - Run test suite"
	@echo "  make test-cov         - Run tests with coverage report"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint             - Run all linters"
	@echo "  make format           - Format code with black and isort"
	@echo ""
	@echo "Database:"
	@echo "  make db-init          - Initialize database"
	@echo "  make db-backup        - Backup database"
	@echo "  make db-clean         - Clean database"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build     - Build Docker image"
	@echo "  make docker-run       - Run Docker container"
	@echo "  make docker-compose   - Run with docker-compose"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean            - Remove build artifacts"
	@echo "  make clean-pyc        - Remove Python cache files"
	@echo ""

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

dev:
	FLASK_ENV=development FLASK_APP=run.py flask run

test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=app --cov-report=html --cov-report=term-missing

lint:
	flake8 app/ tests/ scripts/ --max-line-length=100
	pylint app/ --fail-under=8.0

format:
	black app/ tests/ scripts/
	isort app/ tests/ scripts/

db-init:
	python scripts/init_db.py

db-backup:
	python scripts/backup_db.py

db-clean:
	rm -f certificate_sender.db
	rm -f logs/*.log*

docker-build:
	docker build -f docker/Dockerfile -t certificate-app:latest .

docker-run:
	docker run -p 5000:8000 --env-file .env certificate-app:latest

docker-compose:
	docker-compose -f docker/docker-compose.yml up

clean: clean-pyc clean-test clean-build
	rm -rf htmlcov/
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/

clean-pyc:
	find . -type f -name '*.py[cod]' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -name '*~' -delete

clean-test:
	rm -rf .tox/
	rm -f .coverage
	rm -rf htmlcov/

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/

.DEFAULT_GOAL := help
