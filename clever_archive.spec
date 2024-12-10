Name: clever_archive
Version: 1.0
Release: 1%{?dist}
Summary: Tool for categorizing and organizing files in a directory

# Требования
Requires: python3

# Описание
%description
This tool categorizes files in a directory based on their extensions and organizes them into subfolders.

# Установка
%prep

# Установка
%setup -q

# Сборка
%build

# Установка
%install
mkdir -p %{buildroot}/usr/bin
install -m 755 setup.py %{buildroot}/usr/bin/clever_archive.py

# Каталог файлов
%files
%{_bindir}/clever_archive.py

# Скрипт установки
%post
chmod a+x %{_bindir}/clever_archive.py

%postun
rm -f %{_bindir}/clever_archive.py

