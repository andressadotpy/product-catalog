from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required


from . import admin
from .forms import SellerForm, CategoryForm
from .. import db
from ..models import Seller, Category, Product


def check_admin():
    if not current_user.is_admin:
        abort(403)

#### CRUD FOR SELLER ####

@admin.route('/sellers', methods=['GET', 'POST'])
@login_required
def show_all_sellers():
    sellers = Seller.query.all()
    return render_template('admin/sellers/sellers.html', sellers=sellers)


@admin.route('/sellers/add', methods=['GET', 'POST'])
@login_required
def add_new_seller():
    check_admin()
    form = SellerForm()
    if form.validate_on_submit():
        seller = Seller(seller_name=form.seller_name.data,
                    email=form.seller_email.data,
                    phone=form.seller_phone.data,
                    site=form.seller_site.data)
        try:
            db.session.add(seller)
            db.session.commit()
            flash('You have successfully added a new seller.')
        except:
            flash('Error: this seller is already saved.')
        return redirect(url_for('admin.show_all_sellers'))


@admin.route('/sellers/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_seller(id):
    check_admin()
    seller = Seller.query.get_or_404(id)
    form = SellerForm(obj=seller)
    if form.validate_on_submit():
        seller_name = form.seller_name.data
        email = form.seller_email.data
        phone = form.seller_phone.data
        site = form.seller_site.data
        flash('You have successfully edited a seller.')
        return redirect(url_for('admin.show_all_sellers'))


@admin.route('/sellers/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_seller(id):
    check_admin()
    seller = Seller.query.get_or_404(id)
    db.session.delete(seller)
    db.session.commit()
    flash('The seller was deleted.')
    return redirect(url_for('admin.show_all_sellers'))


#### CRUD FOR CATEGORY ####

@admin.route('/categories', methods=['GET', 'POST'])
@login_required
def show_all_categories():
    categories = Category.query.all()
    return render_template('admin/categories/categories.html', categories=categories)


@admin.route('/categories/add', methods=['GET', 'POST'])
@login_required
def add_new_category():
    check_admin()
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(category_name=form.category.data)
        try:
            db.session.add(category)
            db.session.commit()
            flash('You have successfully added a new category.')
        except:
            flash('Error: this category is already saved.')
        return redirect(url_for('admin.show_all_categories'))


@admin.route('/categories/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_categories(id):
    check_admin()
    category = Category.query.get_or_404(id)
    form = CategoryForm(obj=category)
    if form.validate_on_submit():
        category_name = form.category.data
        flash('You have successfully edited a category.')
        return redirect(url_for('admin.show_all_categories'))


@admin.route('/categories/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_category(id):
    check_admin()
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash('The category was deleted.')
    return redirect(url_for('admin.show_all_categories'))


#### CRUD FOR PRODUCT ####

@admin.route('/products', methods=['GET', 'POST'])
@login_required
def show_all_products():
    products = Product.query.all()
    return render_template('admin/products/products.html', products=products)


@admin.route('/products/add', methods=['GET', 'POST'])
@login_required
def add_new_product():
    check_admin()
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(product_name=form.product_name.data,
                    sellers=form.sellers.data,
                    category_id=form.category.data)
        try:
            db.session.add(product)
            db.session.commit()
            flash('You have successfully added a product.')
        except:
            flash('Something went wronh.')
        return redirect(url_for('admin.show_all_products'))


@admin.route('/products/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_product(id):
    check_admin()
    product = Product.query.get_or_404(id)
    form = ProductForm(obj=seller)
    if form.validate_on_submit():
        product_name = form.product_name.data
        sellers = form.sellers.data
        category = form.category.data
        flash('You have successfully edited a product.')
        return redirect(url_for('admin.show_all_products'))


@admin.route('/products/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_product(id):
    check_admin()
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('The product was deleted.')
    return redirect(url_for('admin.show_all_products'))
