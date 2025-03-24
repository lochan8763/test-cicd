from flask import Blueprint, jsonify

health_check_routes = Blueprint("health_check_routes", __name__)


@health_check_routes.route("/health-check", methods=["GET"])
def health_check():
    """
    Health check endpoint to verify the application's status.

    Returns:
        Response: JSON response with application status and HTTP 200 status code.
    """
    return jsonify({"message": "Application is running!"}), 200