# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'QuestionResponse.sent'
        db.add_column(u'mothers_calendar_questionresponse', 'sent',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding unique constraint on 'Question', fields ['question_text']
        db.create_unique(u'mothers_calendar_question', ['question_text'])

        # Adding unique constraint on 'QuestionType', fields ['q_type']
        db.create_unique(u'mothers_calendar_questiontype', ['q_type'])


    def backwards(self, orm):
        # Removing unique constraint on 'QuestionType', fields ['q_type']
        db.delete_unique(u'mothers_calendar_questiontype', ['q_type'])

        # Removing unique constraint on 'Question', fields ['question_text']
        db.delete_unique(u'mothers_calendar_question', ['question_text'])

        # Deleting field 'QuestionResponse.sent'
        db.delete_column(u'mothers_calendar_questionresponse', 'sent')


    models = {
        u'mothers_calendar.message': {
            'Meta': {'object_name': 'Message'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_text': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'week': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'week_in_cycle'", 'to': u"orm['mothers_calendar.WeekNumber']"})
        },
        u'mothers_calendar.mother': {
            'Meta': {'object_name': 'Mother'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mothers'", 'to': u"orm['rapidsms.Contact']"}),
            'contact_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'week': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'mothers'", 'to': u"orm['mothers_calendar.WeekNumber']"})
        },
        u'mothers_calendar.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'question_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mothers_calendar.QuestionType']"}),
            'week': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'weeks_question'", 'to': u"orm['mothers_calendar.WeekNumber']"})
        },
        u'mothers_calendar.questionresponse': {
            'Meta': {'unique_together': "(('question', 'contact'),)", 'object_name': 'QuestionResponse'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rapidsms.Contact']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'responses'", 'to': u"orm['mothers_calendar.Question']"}),
            'responded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'mothers_calendar.questiontype': {
            'Meta': {'object_name': 'QuestionType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q_type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        u'mothers_calendar.weeknumber': {
            'Meta': {'object_name': 'WeekNumber'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'week_number': ('django.db.models.fields.IntegerField', [], {})
        },
        u'rapidsms.contact': {
            'Meta': {'object_name': 'Contact'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['mothers_calendar']