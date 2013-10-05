# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WeekNumber'
        db.create_table(u'mothers_calendar_weeknumber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('week_number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mothers_calendar', ['WeekNumber'])

        # Adding model 'Message'
        db.create_table(u'mothers_calendar_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message_text', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('week', self.gf('django.db.models.fields.related.ForeignKey')(related_name='week_in_cycle', to=orm['mothers_calendar.WeekNumber'])),
        ))
        db.send_create_signal(u'mothers_calendar', ['Message'])

        # Adding model 'QuestionType'
        db.create_table(u'mothers_calendar_questiontype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q_type', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'mothers_calendar', ['QuestionType'])

        # Adding model 'Question'
        db.create_table(u'mothers_calendar_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mothers_calendar.QuestionType'])),
            ('week', self.gf('django.db.models.fields.related.ForeignKey')(related_name='weeks_question', to=orm['mothers_calendar.WeekNumber'])),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'mothers_calendar', ['Question'])


    def backwards(self, orm):
        # Deleting model 'WeekNumber'
        db.delete_table(u'mothers_calendar_weeknumber')

        # Deleting model 'Message'
        db.delete_table(u'mothers_calendar_message')

        # Deleting model 'QuestionType'
        db.delete_table(u'mothers_calendar_questiontype')

        # Deleting model 'Question'
        db.delete_table(u'mothers_calendar_question')


    models = {
        u'mothers_calendar.message': {
            'Meta': {'object_name': 'Message'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_text': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'week': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'week_in_cycle'", 'to': u"orm['mothers_calendar.WeekNumber']"})
        },
        u'mothers_calendar.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'question_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mothers_calendar.QuestionType']"}),
            'week': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'weeks_question'", 'to': u"orm['mothers_calendar.WeekNumber']"})
        },
        u'mothers_calendar.questiontype': {
            'Meta': {'object_name': 'QuestionType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q_type': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'mothers_calendar.weeknumber': {
            'Meta': {'object_name': 'WeekNumber'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'week_number': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['mothers_calendar']