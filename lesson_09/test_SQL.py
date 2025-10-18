from Subject_API import SubjectAPI
import pytest

db= SubjectAPI("postgresql://postgres:12345@localhost:5433/postgres")


def test_insert_subject():
	db.create(new_subject='Magic')
	db.delete(subject_to_delete='Magic')


def test_update_subject():
	db.create(new_subject='Magic')
	db.update(subject_to_update='Magic', new_id=27)
	db.delete(subject_to_delete='Magic')

def test_delete_subject():
	db.create(new_subject='Transfiguration')
	db.delete(subject_to_delete='Transfiguration')
