# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organization'
        db.create_table(u'directory_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('primary_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=256)),
            ('secondary_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('phone', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('fax', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('state', self.gf('localflavor.us.models.USStateField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal(u'directory', ['Organization'])

        # Adding model 'Person'
        db.create_table(u'directory_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('primary_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('secondary_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('phone', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('state', self.gf('localflavor.us.models.USStateField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal(u'directory', ['Person'])

        # Adding model 'Group'
        db.create_table(u'directory_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('primary_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('secondary_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('parent_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Group'])),
        ))
        db.send_create_signal(u'directory', ['Group'])

        # Adding M2M table for field leaders on 'Group'
        m2m_table_name = db.shorten_name(u'directory_group_leaders')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm[u'directory.group'], null=False)),
            ('person', models.ForeignKey(orm[u'directory.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['group_id', 'person_id'])

        # Adding M2M table for field memebers on 'Group'
        m2m_table_name = db.shorten_name(u'directory_group_memebers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm[u'directory.group'], null=False)),
            ('person', models.ForeignKey(orm[u'directory.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['group_id', 'person_id'])


    def backwards(self, orm):
        # Deleting model 'Organization'
        db.delete_table(u'directory_organization')

        # Deleting model 'Person'
        db.delete_table(u'directory_person')

        # Deleting model 'Group'
        db.delete_table(u'directory_group')

        # Removing M2M table for field leaders on 'Group'
        db.delete_table(db.shorten_name(u'directory_group_leaders'))

        # Removing M2M table for field memebers on 'Group'
        db.delete_table(db.shorten_name(u'directory_group_memebers'))


    models = {
        u'directory.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leaders': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'leaders'", 'symmetrical': 'False', 'to': u"orm['directory.Person']"}),
            'memebers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members'", 'symmetrical': 'False', 'to': u"orm['directory.Person']"}),
            'parent_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['directory.Group']"}),
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