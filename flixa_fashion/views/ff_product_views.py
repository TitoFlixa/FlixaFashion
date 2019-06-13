<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>
        <record id="ff_product_template_only_form_view_inherit" model="ir.ui.view">
            <field name="name">ff.product.template.only.product.form</field>
            <field name="model">product.template</field>
            <field name="priority" eval="8" />
            <field name="inherit_id" ref="product.product_template_only_form_view"/>
            <field name="arch" type="xml">
                <xpath expr="//page[@name='variants']" position="replace">
                    <page name="variants" string="Attributes" groups="product.group_product_variant">
                        <group>
                            <group>
                                <field name="is_size_scale"/>
                                <field name="size_scale_id"
                                       attrs="{'invisible':[('is_size_scale','=',False)]}"/>
                            </group>
                            <group>
                                <field name="value_ids"
                                       widget="many2many_tags"
                                       attrs="{'invisible':[('size_scale_id','=',False)]}"/>
                            </group>
                        </group>
                        <field name="attribute_line_ids" widget="one2many_list"
                               context="{'show_attribute': False}" >
                            <tree string="Variants" editable="bottom">
                                <field name="attribute_id"/>
                                <field name="value_ids" widget="many2many_tags"
                                       domain="[('attribute_id', '=', attribute_id)]"
                                       context="{'default_attribute_id': attribute_id}"/>
                                <field name="is_size_scale_line" readonly="1"/>
                            </tree>
                        </field>
                        <p class="oe_grey">
                            <strong>Warning</strong>: adding or deleting attributes
                            will delete and recreate existing variants and lead
                            to the loss of their possible customizations.
                        </p>
                    </page>

                </xpath>

            </field>
        </record>


    </data>
</odoo>