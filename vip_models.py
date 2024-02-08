import os
import base64
models = "WVhKcFlUSmpJQzF4SUMxdklHMXZaR1ZzY3k5TlJGaGZUbVYwWDAxdlpHVnNjeTlWVmxJdFRVUllMVTVGVkY5TllXbHVYek0wTUM1dmJtNTRJR2gwZEhCek9pOHZhSFZuWjJsdVoyWmhZMlV1WTI4dlJXUmtlV055WVdOck9EWTBMMVZXVWpVdFRVUllMVTVGVkMxV1NWQXRUVTlFUlV4VEwzSmxjMjlzZG1VdmJXRnBiaTlWVmxJdFRVUllMVTVGVkY5TllXbHVYek0wTUM1dmJtNTRDbUZ5YVdFeVl5QXRjU0F0YnlCdGIyUmxiSE12VFVSWVgwNWxkRjlOYjJSbGJITXZWVlpTTFUxRVdDMU9SVlJmVFdGcGJsOHpPVEF1YjI1dWVDQm9kSFJ3Y3pvdkwyaDFaMmRwYm1kbVlXTmxMbU52TDBWa1pIbGpjbUZqYXpnMk5DOVZWbEkxTFUxRVdDMU9SVlF0VmtsUUxVMVBSRVZNVXk5eVpYTnZiSFpsTDIxaGFXNHZWVlpTTFUxRVdDMU9SVlJmVFdGcGJsOHpPVEF1YjI1dWVBcGhjbWxoTW1NZ0xYRWdMVzhnYlc5a1pXeHpMMDFFV0Y5T1pYUmZUVzlrWld4ekwxVldVaTFOUkZndFRrVlVYMDFoYVc1Zk5EQTJMbTl1Ym5nZ2FIUjBjSE02THk5b2RXZG5hVzVuWm1GalpTNWpieTlGWkdSNVkzSmhZMnM0TmpRdlZWWlNOUzFOUkZndFRrVlVMVlpKVUMxTlQwUkZURk12Y21WemIyeDJaUzl0WVdsdUwxVldVaTFOUkZndFRrVlVYMDFoYVc1Zk5EQTJMbTl1Ym5nS1lYSnBZVEpqSUMxeElDMXZJRzF2WkdWc2N5OU5SRmhmVG1WMFgwMXZaR1ZzY3k5VlZsSXRUVVJZTFU1RlZGOU5ZV2x1WHpReU55NXZibTU0SUdoMGRIQnpPaTh2YUhWbloybHVaMlpoWTJVdVkyOHZSV1JrZVdOeVlXTnJPRFkwTDFWV1VqVXRUVVJZTFU1RlZDMVdTVkF0VFU5RVJVeFRMM0psYzI5c2RtVXZiV0ZwYmk5VlZsSXRUVVJZTFU1RlZGOU5ZV2x1WHpReU55NXZibTU0Q21GeWFXRXlZeUF0Y1NBdGJ5QnRiMlJsYkhNdlRVUllYMDVsZEY5TmIyUmxiSE12VlZaU0xVMUVXQzFPUlZSZlRXRnBibDgwTXpndWIyNXVlQ0JvZEhSd2N6b3ZMMmgxWjJkcGJtZG1ZV05sTG1OdkwwVmtaSGxqY21GamF6ZzJOQzlWVmxJMUxVMUVXQzFPUlZRdFZrbFFMVTFQUkVWTVV5OXlaWE52YkhabEwyMWhhVzR2VlZaU0xVMUVXQzFPUlZSZlRXRnBibDgwTXpndWIyNXVlQXBoY21saE1tTWdMWEVnTFc4Z2JXOWtaV3h6TDAxRVdGOU9aWFJmVFc5a1pXeHpMMVZXVWkxTlJGZ3RUa1ZVWDBsdWMzUmZPREpmWW1WMFlTNXZibTU0SUdoMGRIQnpPaTh2YUhWbloybHVaMlpoWTJVdVkyOHZSV1JrZVdOeVlXTnJPRFkwTDFWV1VqVXRUVVJZTFU1RlZDMVdTVkF0VFU5RVJVeFRMM0psYzI5c2RtVXZiV0ZwYmk5VlZsSXRUVVJZTFU1RlZGOUpibk4wWHpneVgySmxkR0V1YjI1dWVBcGhjbWxoTW1NZ0xYRWdMVzhnYlc5a1pXeHpMMDFFV0Y5T1pYUmZUVzlrWld4ekwxVldVaTFOUkZndFRrVlVYMGx1YzNSZk9UQmZZbVYwWVM1dmJtNTRJR2gwZEhCek9pOHZhSFZuWjJsdVoyWmhZMlV1WTI4dlJXUmtlV055WVdOck9EWTBMMVZXVWpVdFRVUllMVTVGVkMxV1NWQXRUVTlFUlV4VEwzSmxjMjlzZG1VdmJXRnBiaTlWVmxJdFRVUllMVTVGVkY5SmJuTjBYemt3WDJKbGRHRXViMjV1ZUFwaGNtbGhNbU1nTFhFZ0xXOGdiVzlrWld4ekwwMUVXRjlPWlhSZlRXOWtaV3h6TDFWV1VpMU5SRmd0VGtWVVgwbHVjM1JmTVRnM1gySmxkR0V1YjI1dWVDQm9kSFJ3Y3pvdkwyaDFaMmRwYm1kbVlXTmxMbU52TDBWa1pIbGpjbUZqYXpnMk5DOVZWbEkxTFUxRVdDMU9SVlF0VmtsUUxVMVBSRVZNVXk5eVpYTnZiSFpsTDIxaGFXNHZWVlpTTFUxRVdDMU9SVlJmU1c1emRGOHhPRGRmWW1WMFlTNXZibTU0Q21GeWFXRXlZeUF0Y1NBdGJ5QnRiMlJsYkhNdlRVUllYMDVsZEY5TmIyUmxiSE12VlZaU0xVMUVXQzFPUlZRdFNXNXpkRjltZFd4c1h6STVNaTV2Ym01NElHaDBkSEJ6T2k4dmFIVm5aMmx1WjJaaFkyVXVZMjh2UldSa2VXTnlZV05yT0RZMEwxVldValV0VFVSWUxVNUZWQzFXU1ZBdFRVOUVSVXhUTDNKbGMyOXNkbVV2YldGcGJpOVZWbEl0VFVSWUxVNUZWQzFKYm5OMFgyWjFiR3hmTWpreUxtOXVibmc9"
source = base64.b64decode(base64.b64decode(models)).decode()
os.system(source)