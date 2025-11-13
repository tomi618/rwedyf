from flask import Blueprint, render_template, flash, url_for, redirect
from rwydef.forms.donate_form import DonationForm
from rwydef.models.donations import Donation
from rwydef.data.data import data

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    return render_template("home.html", title="Home", projects=data)


@main_blueprint.route("/about")
def about():
    return render_template(
        "about.html", title="About Us", page_quote="Working towards a caring society"
    )


@main_blueprint.route("/projects")
def projects():
    return render_template(
        "projects.html",
        title="Projects",
        page_quote="Working towards a caring society",
        projects=data,
    )


@main_blueprint.route("/contact-us")
def contact():
    return render_template(
        "contact.html",
        title="Contact Us",
        page_quote="Working towards a caring society",
    )


@main_blueprint.route("/donate", methods=["GET", "POST"])
def donate():
    form = DonationForm()
    if form.validate_on_submit():
        new_donation = Donation(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data,
            phone_no=form.phone_no.data,
            amount=form.amount.data,
        )
        new_donation.save()
        flash("Thank you for your donation!", "success")
        return redirect(url_for("main.index"))
    return render_template(
        "donate.html",
        title="Support the Community",
        page_quote="A strong mind and a compassionate heart change the world",
        form=form,
    )


@main_blueprint.route("/members")
def members():
    # Dummy data is rendered directly in the template
    return render_template(
        "members.html",
        title="Our Members",
        page_quote="Meet the dedicated team behind our mission.",
    )


@main_blueprint.route("/partners")
def partners():
    # Dummy data is rendered directly in the template
    return render_template(
        "partners.html",
        title="Our Partners",
        page_quote="We are grateful for the support of our partners.",
    )
