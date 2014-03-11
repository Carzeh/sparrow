# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MenuItem'
        db.create_table(u'menuapp_menuitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('price', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('second_price', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'menuapp', ['MenuItem'])

        # Adding model 'Drink'
        db.create_table(u'menuapp_drink', (
            (u'menuitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['menuapp.MenuItem'], unique=True, primary_key=True)),
            ('is_soft', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_hard', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'menuapp', ['Drink'])

        # Adding model 'Food'
        db.create_table(u'menuapp_food', (
            (u'menuitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['menuapp.MenuItem'], unique=True, primary_key=True)),
            ('is_dinner', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_brunch', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_side', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'menuapp', ['Food'])


    def backwards(self, orm):
        # Deleting model 'MenuItem'
        db.delete_table(u'menuapp_menuitem')

        # Deleting model 'Drink'
        db.delete_table(u'menuapp_drink')

        # Deleting model 'Food'
        db.delete_table(u'menuapp_food')


    models = {
        u'menuapp.drink': {
            'Meta': {'object_name': 'Drink', '_ormbases': [u'menuapp.MenuItem']},
            'is_hard': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_soft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'menuitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['menuapp.MenuItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'menuapp.food': {
            'Meta': {'object_name': 'Food', '_ormbases': [u'menuapp.MenuItem']},
            'is_brunch': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_dinner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_side': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'menuitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['menuapp.MenuItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'menuapp.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'price': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'second_price': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['menuapp']