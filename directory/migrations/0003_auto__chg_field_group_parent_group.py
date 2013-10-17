# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Group.parent_group'
        db.alter_column(u'directory_group', 'parent_group_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Group'], null=True))

    def backwards(self, orm):

        # Changing field 'Group.parent_group'
        db.alter_column(u'directory_group', 'parent_group_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['directory.Group']))

    models = {
        u'directory.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leaders': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'leaders'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['directory.Person']"}),
            'memebers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'members'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['directory.Person']"}),
            'parent_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['directory.Group']", 'null': 'True', 'blank': 'True'}),
            'primary_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'secondary_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'directory.organization': {
            'Meta': {'object_name': 'Organization'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fax': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'primary_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'}),
            'secondary_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        },
        u'directory.person': {
            'Meta': {'object_name': 'Person'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'primary_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'secondary_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['directory']