##
#
# db_model.py is a Class collection to model the db, using sqlalchemy.
#
# Copyright (C) 2016 - Internet Archive
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##

"""
db_model.py

database model for the database

:    author: Giovanni Damiola <gio@archive.org>
: copyright: (c) 2016 Internet Archive.
:   license: AGPL 3, see LICENSE for more details.
"""

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import JSON, JSONB
from sqlalchemy.orm import relationship
from database import Base

import datetime


class JsonTable(Base):
    __abstract__ = True
    identifier = Column(String(100), primary_key=True)
    document = Column(JSON, nullable=False)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


    def __init__(self, identifier=None, document=None):
        self.identifier = identifier
        self.document = document

    def __repr__(self):
        return '<%r>' % (self.identifier)


class Books(JsonTable):
    __tablename__ = 'iabbooks'


class Events(JsonTable):
    __tablename__ = 'iabevents'
    identifier = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self, document=None):
        self.document = document


    __tablename__ = 'iabscancenters'
