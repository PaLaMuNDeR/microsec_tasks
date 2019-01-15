from django.shortcuts import render, redirect
from .models import Temperature


def temperature(request):
    """
    Temperature view - shows the temperature's value with latest value.

    The template for this view has the WebSocket business to send and stream
    value.
    """

    # We want to show the last 50 messages, ordered most-recent-last
    values = reversed(Temperature.objects.order_by('-timestamp')[:50])

    return render(request, "task_3/temperature.html", {
        'values': values,
    })
