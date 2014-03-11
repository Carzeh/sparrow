# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MenuItem.price'
        db.alter_column(u'menuapp_menuitem', 'price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

        # Changing field 'MenuItem.second_price'
        db.alter_column(u'menuapp_menuitem', 'second_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'MenuItem.price'
        db.alter_column(u'menuapp_menuitem', 'price', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4))

        # Changing field 'MenuItem.second_price'
        db.alter_column(u'menuapp_menuitem', 'second_price', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True))

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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'second_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['menuapp']