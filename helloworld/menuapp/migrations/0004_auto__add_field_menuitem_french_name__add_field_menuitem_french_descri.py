# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MenuItem.french_name'
        db.add_column(u'menuapp_menuitem', 'french_name',
                      self.gf('django.db.models.fields.CharField')(default='name', max_length=150),
                      keep_default=False)

        # Adding field 'MenuItem.french_description'
        db.add_column(u'menuapp_menuitem', 'french_description',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MenuItem.french_name'
        db.delete_column(u'menuapp_menuitem', 'french_name')

        # Deleting field 'MenuItem.french_description'
        db.delete_column(u'menuapp_menuitem', 'french_description')


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
            'french_description': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'french_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'second_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['menuapp']