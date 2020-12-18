from django.contrib import admin
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib import messages
from django.conf.urls import url
from .models import CustomUser, ManagerRight, ManagerProfile, EmployeeProfile, Skill, SessionLogs, Certification, FuturePlan, Responce, LiveInteraction, BroadcastMessage, AdminMessage
from .forms import CustomUserCreationFormManager,CustomUserCreationFormEmployee
from .utils import Util
from django.contrib.admin import AdminSite
from django.core import mail
from django.utils.translation import ugettext_lazy
import nested_inline.admin as nested_admin
import string
import random
import io
import csv
from django.core.mail import get_connection, EmailMultiAlternatives




def emailTemp(email, password, msg):
    sty = '''
    <head>
        <style>

            @media(min-width: 600px){
                .margin{
                    width:44%;
                    margin:auto;
                }
            }
        </style>
    </hesd>
    '''
    template = f'''
        {sty}

        <div class="margin">
        <table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%">
          <tbody>
            <tr>
              <td style="padding:3.75pt 0cm 0cm 0cm">
                <div>
                  <div>
                    <div align="center">
                      <table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%">
                        <tbody>
                          <tr>
                            <td style="padding:0cm 0cm 0cm 0cm">
                              <p class="MsoNormal" align="center" style="text-align:center">
                                <a href="https://engagenreap.com/" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://engagenreap.com/&amp;source=gmail&amp;ust=1607938525597000&amp;usg=AFQjCNE2Lm3fkzk156etaNapsRTyxVPtdQ"><span style="color:windowtext;text-decoration:none"><span style="color:blue"><img border="0" width="500" style="width:5.2083in" id="m_-6143579707687088962m_9048336023720413984m_6655452115838635839_x0000_i1033" src="https://ci6.googleusercontent.com/proxy/IrinkoH9AEanQle2obJGZR5MBo9eIVIK7uBOJkaKojwY5tyBnRwBZxFLGfo_SUkjioyOeXjRuBIJT1NdGr8RAUhsXxve5yLuHje_ZqUR0M8t37AFOnK0fjQTmYtg4mrVQEjJvUJuX7Zw6bJw-SvNpQBs_h_NtIOKeg=s0-d-e1-ft#https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/BeeProAgency/561156_542492/header_1.jpg" alt="Alternate text" class="CToWUd"></span></span></a><u></u><u></u></p>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                      <p class="MsoNormal" style="vertical-align:top"><span style="display:none"><u></u>&nbsp;<u></u></span></p>
                      <table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%">
                        <tbody>
                          <tr>
                            <td style="padding:7.5pt 7.5pt 7.5pt 7.5pt">
                              <div>
                                <div>
                                  <p style="margin:0cm;line-height:19.5pt;word-break:break-word"><span style="font-size:15.5pt;font-family:&quot;Arial&quot;,sans-serif;font-weight:800;color:#555555">Welcome to EnR Consultancy Services<u></u><u></u></span></p>
                                  <p style="font-size:13.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555">{msg}</p>
                                  <p style="font-size:11.5pt;font-family:&quot;Arial&quot;,sans-serif;font-weight:600;color:#000000">Username: {email}</p>
                                  <p style="font-size:11.5pt;font-family:&quot;Arial&quot;,sans-serif;font-weight:600;color:#000000">Password: {password}</p>
                                  <p style="margin:0cm;word-break:break-word"><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><br>
                                  </span><span style="font-size:13.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555">Greetings from Engage and Reap(EnR) Consultancy Services, IT and Consulting Company headquartered in Milton Keynes, UK.</span><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><u></u><u></u></span></p>
                                  <p align="center" style="margin:0cm;text-align:center;word-break:break-word">
                                    <span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><br>
                                    </span><strong><span style="font-size:13.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555">“Customer Success is our Mission!”</span></strong><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><u></u><u></u></span></p>
                                    <p style="margin:0cm;word-break:break-word"><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><br>
                                    </span><span style="font-size:13.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555">IT and Business Consulting just for you. Business progress at the speed of light only at EnR. We provided services to industries like Financial Services, Automotive, Retail,
                                      Logistics, Packaging, Manufacturing, and many more.</span><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><u></u><u></u></span></p>
                                      <p style="margin:0cm;word-break:break-word"><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><br>
                                      </span><span style="font-size:13.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555">IT Consulting at EnR helps to build Digital Transformation. Issues from Disaster Management to Network Operations, EnR provides the best solutions.</span><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><u></u><u></u></span></p>
                                      <p align="center" style="margin:0cm;text-align:center;word-break:break-word">
                                        <span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><br>
                                        </span><strong><span style="font-size:13.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555">“13 Years of experience!!”</span></strong><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><u></u><u></u></span></p>
                                        <p align="center" style="margin:0cm;text-align:center;word-break:break-word">
                                          <strong><span style="font-size:13.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555">“50 Customers Served!!”</span></strong><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><u></u><u></u></span></p>
                                          <p align="center" style="margin:0cm;text-align:center;word-break:break-word">
                                            <span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555">&nbsp;<u></u><u></u></span></p>
                                            <p style="margin:0cm;line-height:19.5pt;word-break:break-word"><span style="font-size:13.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555">We are a one-stop-shop for all issues. Along with these advantages, what makes EnR Consultancy Services unique is our
                                              flawless integration and fit-for-purpose solutions. We never compromise on quality and we provide the best-in-class service within your budget.&nbsp;<u></u><u></u></span></p>
                                              <p align="center" style="margin:0cm;text-align:center;word-break:break-word">
                                                <span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><br>
                                                </span><strong><span style="font-size:13.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555">“We engage, You reap!”</span></strong><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><u></u><u></u></span></p>
                                                <p style="margin:0cm;word-break:break-word"><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><br>
                                                </span><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#555555"><u></u><u></u></span></p>
                                              </div>
                                            </div>
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                    <p class="MsoNormal" align="center" style="text-align:center;vertical-align:top">
                                      <span style="display:none"><u></u>&nbsp;<u></u></span></p>
                                      <div align="center">
                                        <table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse;border-spacing:0">
                                          <tbody>
                                            <tr>
                                              <td style="padding:7.5pt 7.5pt 7.5pt 7.5pt">
                                                <p class="MsoNormal" align="center" style="text-align:center"><u></u><span><map name="m_-6143579707687088962_m_9048336023720413984_m_6655452115838635839_MicrosoftOfficeMap0"></map></span><u></u><u></u><u></u></p>
                                              </td>
                                            </tr>
                                          </tbody>
                                        </table>
                                      </div>
                                      <p class="MsoNormal" style="vertical-align:top"><u></u>&nbsp;<u></u></p>
                                      <table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse;border-spacing:0px">
                                        <tbody>
                                          <tr style="display:inline-block">
                                            <td valign="top" style="padding:7.5pt 7.5pt 7.5pt 7.5pt;word-break:break-word">
                                              <div align="center">
                                                <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;word-break:break-word">
                                                  <tbody>
                                                    <tr style="word-break:break-word">
                                                      <td valign="top" style="padding:0cm 3.0pt 0cm 3.0pt;border-spacing:0">
                                                        <p class="MsoNormal" align="center" style="text-align:center"><a href="https://engagenreap.com/" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://engagenreap.com/&amp;source=gmail&amp;ust=1607938525597000&amp;usg=AFQjCNE2Lm3fkzk156etaNapsRTyxVPtdQ"><span style="color:windowtext;text-decoration:none"><span style="color:blue"><img border="0" width="32" height="32" style="width:.3333in;height:.3333in" id="m_-6143579707687088962m_9048336023720413984m_6655452115838635839_x0000_i1031" src="https://ci6.googleusercontent.com/proxy/B_5rcD_jdAYUlmEYfyA9IMfAMBq7rQRJmWTCpxUDRPukXt-ZB1l54tZbN2KdvHruBiWRWLOdiG2M3CyZ64QT4AIOnKUliFyXX6JOLu7EOEcXobQBu9Oh9O3QVRGDkLQVlcyHFbSMnm5DNR4z3bdwl383hKkG=s0-d-e1-ft#https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/BeeProAgency/561156_542492/logo.png" alt="Custom" class="CToWUd"></span></span></a><u></u><u></u></p>
                                                      </td>
                                                      <td valign="top" style="padding:0cm 3.0pt 0cm 3.0pt;word-break:break-word">
                                                        <p class="MsoNormal" align="center" style="text-align:center"><a href="https://www.facebook.com/EnRConsultancyServices" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.facebook.com/EnRConsultancyServices&amp;source=gmail&amp;ust=1607938525597000&amp;usg=AFQjCNGLpzjouOARFNy55eBTxRLUHN57fw"><span style="color:windowtext;text-decoration:none"><span style="color:blue"><img border="0" width="32" height="32" style="width:.3333in;height:.3333in" id="m_-6143579707687088962m_9048336023720413984m_6655452115838635839_x0000_i1030" src="https://ci4.googleusercontent.com/proxy/9Deo1O4asmCneCulBuSA2dH7zkOIIbIZ8WBkxA4IfEMdk2fLSj63glUNGdcBQU9OLVxmwFkVeN6WOka3UJ0-TxWb7wsM0B1CbeIvcSvJabDVkqiR2v4KP-oicr61BmSwgZ4A6pM761HsddHvZP9MMNUH8deDmX635wwHywtXko8=s0-d-e1-ft#https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/circle-color/facebook@2x.png" alt="Facebook" class="CToWUd"></span></span></a><u></u><u></u></p>
                                                      </td>
                                                      <td valign="top" style="padding:0cm 3.0pt 0cm 3.0pt;word-break:break-word">
                                                        <p class="MsoNormal" align="center" style="text-align:center"><a href="https://twitter.com/services_enr" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://twitter.com/services_enr&amp;source=gmail&amp;ust=1607938525597000&amp;usg=AFQjCNE-0OUObMJIvxKR4J-T_JzL3MkH5Q"><span style="color:windowtext;text-decoration:none"><span style="color:blue"><img border="0" width="32" height="32" style="width:.3333in;height:.3333in" id="m_-6143579707687088962m_9048336023720413984m_6655452115838635839_x0000_i1029" src="https://ci5.googleusercontent.com/proxy/FI1DQz52WPNyLGbiey2GDE-9UwZFKcDt2NqoTPr-7E9gKsYwbGwfa2GbCmo9VkA36V9T1I-Yx7X2qt79rmA-jdGFnzFH1x3o7QcAaggVUfUIvdlu9XCJf2JrYKXiCHBX8OtjBnVsKzlSz9QwBHeFV_rOOR279LcbmYHAJWmtIg=s0-d-e1-ft#https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/circle-color/twitter@2x.png" alt="Twitter" class="CToWUd"></span></span></a><u></u><u></u></p>
                                                      </td>
                                                      <td valign="top" style="padding:0cm 3.0pt 0cm 3.0pt;word-break:break-word">
                                                        <p class="MsoNormal" align="center" style="text-align:center"><a href="https://www.instagram.com/enrconsultancyservices/" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.instagram.com/enrconsultancyservices/&amp;source=gmail&amp;ust=1607938525597000&amp;usg=AFQjCNGQ4zPg9nKXfZ-m2bRkYkY8Pati_g"><span style="color:windowtext;text-decoration:none"><span style="color:blue"><img border="0" width="32" height="32" style="width:.3333in;height:.3333in" id="m_-6143579707687088962m_9048336023720413984m_6655452115838635839_x0000_i1028" src="https://ci5.googleusercontent.com/proxy/JnVBDuWoB86nDakRbB8DyKWNvMyjQYVHHS7m-FgGvYTJYlnpZgcJ9baqIQ7n5reueIVJEaVRlpiN80JYzpe43lPq1ILM1LCDaMDhnYRpHB_SvBRgAjxgMv9nCdJdI-CjeUFaF5kdF1SdlRwwH84jwO44YDiUoG9Q-RZ5j2-Y_RMX=s0-d-e1-ft#https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/circle-color/instagram@2x.png" alt="Instagram" class="CToWUd"></span></span></a><u></u><u></u></p>
                                                      </td>
                                                      <td valign="top" style="padding:0cm 3.0pt 0cm 3.0pt;word-break:break-word">
                                                        <p class="MsoNormal" align="center" style="text-align:center"><a href="https://www.linkedin.com/company/engage-reap-consultancy-services/" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.linkedin.com/company/engage-reap-consultancy-services/&amp;source=gmail&amp;ust=1607938525597000&amp;usg=AFQjCNEJoJ8CHfSVfSf3euq5LtzMLFi07g"><span style="color:windowtext;text-decoration:none"><span style="color:blue"><img border="0" width="32" height="32" style="width:.3333in;height:.3333in" id="m_-6143579707687088962m_9048336023720413984m_6655452115838635839_x0000_i1027" src="https://ci6.googleusercontent.com/proxy/HDf7LKd44n0C4xRZlxzCEeAN14UmNi5KioIavIHnWJoj4vKq6Mjm1nLAN-jEVzn0Hrexr4OShK8SCyqfsmwcZaUsOF7EPj9VLp9-56iptYew58JPFHHSXMVKekkilsYFbXPwq2yow8DNwBjC2Zw-vRjSnsSNxgHriNC7FyWk3aY=s0-d-e1-ft#https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/circle-color/linkedin@2x.png" alt="LinkedIn" class="CToWUd"></span></span></a><u></u><u></u></p>
                                                      </td>
                                                      <td valign="top" style="padding:0cm 3.0pt 0cm 3.0pt;word-break:break-word">
                                                        <p class="MsoNormal" align="center" style="text-align:center"><a href="https://medium.com/@EnRConsultancyServices" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://medium.com/@EnRConsultancyServices&amp;source=gmail&amp;ust=1607938525597000&amp;usg=AFQjCNH4vEDMzN21QLfaNEiWDef-Js-X-A"><span style="color:windowtext;text-decoration:none"><span style="color:blue"><img border="0" width="32" height="32" style="width:.3333in;height:.3333in" id="m_-6143579707687088962m_9048336023720413984m_6655452115838635839_x0000_i1026" src="https://ci4.googleusercontent.com/proxy/cWYLG5m7H0FKlSW5mWCWkuiZsnUITfklqMXRUmGcu1Jw4B2kC83PvjkemIW96hEfrSbR13KmyHc_Nl9Bm3VOlRk6Qesgju8v898UStvQTbuVljyGoNfjBoyXw2_qaBF5wY1g75kW7YaHqROd63-TWw_Cy-iYfo47iMUlAoNi=s0-d-e1-ft#https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/circle-color/medium@2x.png" alt="Medium" class="CToWUd"></span></span></a><u></u><u></u></p>
                                                      </td>
                                                      <td valign="top" style="padding:0cm 3.0pt 0cm 3.0pt;word-break:break-word">
                                                        <p class="MsoNormal" align="center" style="text-align:center"><a href="https://www.youtube.com/channel/UCfK_1VsaSyxQwcFhacPE8tw" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.youtube.com/channel/UCfK_1VsaSyxQwcFhacPE8tw&amp;source=gmail&amp;ust=1607938525597000&amp;usg=AFQjCNEPZGQPxQAXq1FNNVro-7l0Mt_GbA"><span style="color:windowtext;text-decoration:none"><span style="color:blue"><img border="0" width="32" height="32" style="width:.3333in;height:.3333in" id="m_-6143579707687088962m_9048336023720413984m_6655452115838635839_x0000_i1025" src="https://ci3.googleusercontent.com/proxy/VCwXmYraU1ze0eeZ79VTJKlBqwFvdcnLbSckv_onti1JVgfvDVjzbNAagPzrrxUZAKjIeBJD2Kez9LDSx-7a46EK7fekY1MXktddEOGljsQZGgq29Qnpkoo57YrEInViTtuB_yl_OjIWS4HBq1-qdn9ON8V63apwafjDPjyzIA=s0-d-e1-ft#https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/circle-color/youtube@2x.png" alt="YouTube" class="CToWUd"></span></span></a><u></u><u></u></p>
                                                      </td>
                                                    </tr>
                                                  </tbody>
                                                </table>
                                              </div>
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </div>
                                  </div>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                          </div>
    '''
    return template





def send_mass_html_mail(datatuple, fail_silently=False, user=None, password=None,
                        connection=None):
    """
    Given a datatuple of (subject, text_content, html_content, from_email,
    recipient_list), sends each message to each recipient list. Returns the
    number of emails sent.

    If from_email is None, the DEFAULT_FROM_EMAIL setting is used.
    If auth_user and auth_password are set, they're used to log in.
    If auth_user is None, the EMAIL_HOST_USER setting is used.
    If auth_password is None, the EMAIL_HOST_PASSWORD setting is used.

    """
    connection = connection or get_connection(
        username=user, password=password, fail_silently=fail_silently)
    messages = []
    for subject, text, html, from_email, recipient in datatuple:
        message = EmailMultiAlternatives(subject, text, from_email, recipient)
        message.attach_alternative(html, 'text/html')
        messages.append(message)
    return connection.send_messages(messages)


class SkillsInline(nested_admin.NestedTabularInline):
    model = Skill
    sortable_field_name = 'employee'
    extra = 0
    fieldsets = (
            (
                'skills', {
                'classes': ('collapse',),
                'fields': ('skill','rating')
                }
            ),
        )

class ManagerProfileInline(nested_admin.NestedStackedInline):
    model = ManagerProfile
    sortable_field_name = 'employee'
    extra = 0

class CertificationInline(nested_admin.NestedStackedInline):
    model = Certification
    extra = 0
    sortable_field_name = 'employee'

class FuturePlanInline(nested_admin.NestedStackedInline):
    model = FuturePlan
    extra = 0
    sortable_field_name = 'employee'

class ResponceInline(nested_admin.NestedStackedInline):
    model = Responce
    extra = 0
    sortable_field_name = 'employee'

class LiveInteractionInline(nested_admin.NestedStackedInline):
    model = LiveInteraction
    extra = 0
    sortable_field_name = 'employee'

class MEmployeeProfileInline(nested_admin.NestedStackedInline):
    model = EmployeeProfile
    sortable_field_name = 'user'
    inlines = [ManagerProfileInline, SkillsInline, CertificationInline, FuturePlanInline, LiveInteractionInline, ResponceInline]
    fieldsets = (
        (
            None, {
                'classes': ('extrapreety',),
                'fields': ('role',)
            }
        ),
        (
            'CV Details', {
                'classes': ('collapse',),
                'fields': ('cv', 'cv_approved', 'cv_defects')
            }
        ),
        (
            'Phone Details', {
                'classes': ('collapse',),
                'fields': ('phone_no', 'phone_approved', 'phone_defects')
            }
        ),
        (
            'Address Details', {
                'classes': ('collapse',),
                'fields': ('address', 'address_approved', 'address_defects')
            }
        ),
        (
            'Govt. Issued Id Details', {
                'classes': ('collapse',),
                'fields': ('govt_issued_id', 'govt_issued_id_approved', 'govt_issued_id_defects')
            }
        ),
    )

class EmployeeProfileInline(nested_admin.NestedStackedInline):
    model = EmployeeProfile
    sortable_field_name = 'user'
    inlines = [SkillsInline, CertificationInline, FuturePlanInline, LiveInteractionInline, ResponceInline]
    fieldsets = (
        (
            None, {
                'classes': ('extrapreety',),
                'fields': ('role',)
            }
        ),
        (
            'CV Details', {
                'classes': ('collapse',),
                'fields': ('cv', 'cv_approved', 'cv_defects')
            }
        ),
        (
            'Phone Details', {
                'classes': ('collapse',),
                'fields': ('phone_no', 'phone_approved', 'phone_defects')
            }
        ),
        (
            'Address Details', {
                'classes': ('collapse',),
                'fields': ('address', 'address_approved', 'address_defects')
            }
        ),
        (
            'Govt. Issued Id Details', {
                'classes': ('collapse',),
                'fields': ('govt_issued_id', 'govt_issued_id_approved', 'govt_issued_id_defects')
            }
        ),
    )

class Manager(CustomUser):
    class Meta:
        proxy = True

class ManagerUserAdmin(nested_admin.NestedModelAdmin):
    model = CustomUser
    add_form = CustomUserCreationFormManager
    list_display = ('email', 'is_active', 'is_manager', 'department')
    list_filter = ('department',)
    fieldsets = (
        (None, {'fields': ('email', 'department')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    inlines = (MEmployeeProfileInline,)
    add_fieldsets = (
        ("Add Manager", {
            'classes': ('wide',),
            'fields': ('email', 'department', 'password')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    change_list_template = 'admin/EmpApp/Manager/change_list.html'

    def get_urls(self):
        urls = super(ManagerUserAdmin, self).get_urls()
        custom_urls = [
            url(r'add/bulk$', self.bulk_manager, name="bulk_manager"),
        ]
        return urls + custom_urls


    def bulk_manager(self, request):
        context = dict(
            self.admin_site.each_context(request), # Include common variables for rendering the admin template.
            something="site",
        )
        context['title'] = 'Bulk Managers'
        context['posttitle'] = 'Upload a CSV file with atleast the columns written below: '
        print(request.user.is_authenticated)
        if request.method=='POST':
            if request.user.is_authenticated and request.user.is_staff:
                file = request.FILES['file']
                decoded_file = file.read().decode('utf-8')
                io_string = io.StringIO(decoded_file)
                print(file)
                csv_file = csv.reader(io_string, delimiter=';', quotechar='|')
                email_i = -99
                department_i = -99
                for row in csv_file:
                    print(row[0].split(","), "first")
                    for i in range(len(row[0].split(","))):
                        if 'email' in row[0].split(",")[i]:
                            email_i = i
                        if 'department' in row[0].split(",")[i]:
                            department_i = i
                        if email_i and department_i:
                            break
                    break
                new_users = []
                if(email_i>=0 and department_i>=0):
                    for row in csv_file:
                        row_l = row[0].split(",")
                        paslen = random.choice([6,7,8,9,10])
                        password = self.randomPass(paslen)
                        HOST = request.META["HTTP_ORIGIN"]
                        email = row_l[email_i]
                        department = row_l[department_i]
                        user = CustomUser.objects.create_user(email=email, password=password, department=department, is_employee=True, is_manager=True)
                        emp = EmployeeProfile.objects.create(user = user, role = "MANAGER")
                        ManagerProfile.objects.create(employee=emp, some="A Manager" )
                        print(request.META['HTTP_ORIGIN'])
                        msg =  f"You are now a part of this organisation ,working as a {department} MANAGER and for easier management of all your work related things you can use our inhouse management solution using following credentials at {request.META['HTTP_ORIGIN']}"
                        new_users.append(
                            (
                                'Welcome to EnR Consultancy Services',

                                '',

                                emailTemp(email, password, msg),

                                'pkkapoor98@gmail.com',

                                [email]
                            )
                        )
                    print(new_users)
                    results = send_mass_html_mail(tuple(new_users))
                    messages.add_message(request, messages.INFO, f'{len(new_users)} Managers added successfully')
                    return HttpResponseRedirect('/admin/EmpApp/manager/')
                messages.error(request, "The CSV File doesn't have one of the 2 required columns")
                return render(request, 'admin/EmpApp/Manager/Bulk_add.html', context)
            return redirect('admin:login')
        return render(request, 'admin/EmpApp/Manager/Bulk_add.html', context)

    def randomPass(self, n):
        letters = string.ascii_lowercase + string.ascii_uppercase
        password = ''.join(random.choice(letters) for i in range(n))
        return password

    def get_queryset(self, request):
        return self.model.objects.filter(is_manager=True).exclude(is_staff=True)


    def save_model(self, request, obj, form, change):
        obj.is_manager = True
        obj.is_employee = True
        department = obj.department
        paslen = random.choice([6,7,8,9,10])
        password = self.randomPass(paslen)
        HOST = request.META["HTTP_ORIGIN"]
        if(len(CustomUser.objects.filter(email=obj.email))==0):
            msg = f'You are now a part of this organisation ,working as a {department} MANAGER and for easier management of all your work related things you can use our inhouse management solution using following credentials at {HOST}'
            obj.set_password(password)
            data = {}
            data['to_email'] = obj.email
            data['email_subject'] = 'Welcome to EnR Consultancy Services'
            data['email_body'] = emailTemp(obj.email, password, msg)
            Util.sendMail(data)
        print(obj)
        super().save_model(request, obj, form, change)

class Employee(CustomUser):
    class Meta:
        proxy = True

class EmployeeAdmin(nested_admin.NestedModelAdmin):
    model = CustomUser
    add_form = CustomUserCreationFormEmployee
    list_display = ('employee_id', 'email', 'is_active', 'is_employee')
    list_filter = ('is_active',)
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_manager')}),
    )
    inlines = [EmployeeProfileInline]

    add_fieldsets = (
        ("Add Employee", {
            'classes': ('wide',),
            'fields': ('email',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    change_list_template = 'admin/EmpApp/Employee/change_list.html'

    def get_urls(self):
        urls = super(EmployeeAdmin, self).get_urls()
        custom_urls = [
            url(r'add/bulk$', self.bulk_employee, name="bulk_employee"),
        ]
        return urls + custom_urls


    def randomPass(self, n):
        letters = string.ascii_lowercase + string.ascii_uppercase
        password = ''.join(random.choice(letters) for i in range(n))
        return password

    def bulk_employee(self, request):
        context = dict(
            self.admin_site.each_context(request), # Include common variables for rendering the admin template.
            something="site",
        )
        context['title'] = 'Bulk Employees'
        context['posttitle'] = 'Upload a CSV file with atleast the columns written below: '
        if request.method=='POST':
            if request.user.is_authenticated and request.user.is_staff:
                file = request.FILES['file']
                decoded_file = file.read().decode('utf-8')
                io_string = io.StringIO(decoded_file)
                print(file)
                csv_file = csv.reader(io_string, delimiter=';', quotechar='|')
                email_i = 0
                role_i = 0

                for row in csv_file:
                    print(row[0].split(","), "first")
                    for i in range(len(row[0].split(","))):
                        if 'email' in row[0].split(",")[i]:
                            email_i = i
                        if 'role' in row[0].split(",")[i]:
                            role_i = i
                        if email_i and role_i:
                            break
                    break

                new_users = []
                for row in csv_file:
                    row_l = row[0].split(",")
                    print(row_l, role_i, "second")
                    paslen = random.choice([6,7,8,9,10])
                    password = self.randomPass(paslen)
                    HOST = request.META["HTTP_ORIGIN"]
                    email = row_l[email_i]
                    user = CustomUser.objects.create_user(email=email, password=password, is_employee=True)
                    EmployeeProfile.objects.create(user = user, role = row_l[role_i])
                    msg = f"You are now a part of this organisation ,working as a {row_l[role_i]} and for easier management of all your work related things you can use our inhouse management solution using following credentials at {HOST}"
                    new_users.append(
                        (
                            'Welcome to EnR Consultancy Services',
                            '',
                            emailTemp(email, password, msg),
                            'pkkapoor98@gmail.com',
                            [email]
                        )
                    )
                print(new_users)
                results = mail.send_mass_mail(tuple(new_users))
                return HttpResponseRedirect('/admin/EmpApp/employee/')
            return redirect('admin:login')
        return render(request, 'admin/EmpApp/Employee/Bulk_add.html', context)



    def get_queryset(self, request):
        return self.model.objects.filter(is_employee=True).exclude(is_manager=True)


    def save_model(self, request, obj, form, change):
        obj.is_employee = True
        paslen = random.choice([6,7,8,9,10])
        password = self.randomPass(paslen)
        HOST = request.META["HTTP_ORIGIN"]
        if(len(CustomUser.objects.filter(email=obj.email))==0):
            msg = f'You are now a part of this organisation and for easier management of all your work related things you can use our inhouse management solution using following credentials at {HOST}'
            obj.set_password(password)
            data = {}
            data['to_email'] = obj.email
            data['email_subject'] = 'Welcome to EnR Consultancy Services'
            data['email_body'] = emailTemp(obj.email, password, msg)
            Util.sendMail(data)
        print(obj)
        super().save_model(request, obj, form, change)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('employee_id', 'email', 'is_active', 'is_employee', 'is_manager', 'department')
    list_filter = ('is_active', 'is_employee', 'is_manager', 'department')
    fieldsets = (
        (None, {'fields': ('email','name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_manager', 'is_employee')}),
    )
    add_fieldsets = (
        ("Add User", {
            'classes': ('wide',),
            'fields': ('email', 'is_active', 'is_staff', 'is_employee', 'is_manager', 'department', 'password')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    def has_add_permission(self, request):
        return False

class SessionLogsAdmin(admin.ModelAdmin):
    model = SessionLogs
    list_display = ('user', 'login_time', 'logout_time', 'session_time')

    def session_time(self, obj):
        try:
            return obj.logout_time - obj.login_time
        except:
            return "Still Logged In"

class AdminMessageAdmin(admin.ModelAdmin):
    model = AdminMessage
    list_display = ('to', 'message', 'seen')

    fieldsets = (
        ("Send Message", {
            'classes': ('wide',),
            'fields': ('to', 'message')}
        ),
    )



class AdminMessageInline(nested_admin.NestedTabularInline):
    model = AdminMessage
    sortable_field_name = 'to'
    extra = 1
    fieldsets = (
            (
                'Message', {
                'classes': ('collapse',),
                'fields': ('message',)
                }
            ),
        )


class BroadcastMessageAdmin(admin.ModelAdmin):
    model = BroadcastMessage
    list_display = ('message',)
    fieldsets = (
        ("Send Broadcast Message", {
            'classes': ('wide',),
            'fields': ('to','message')}
        ),
    )


admin.site.register(BroadcastMessage, BroadcastMessageAdmin)
admin.site.register(AdminMessage, AdminMessageAdmin)
admin.site.register(SessionLogs, SessionLogsAdmin)
admin.site.register(Manager, ManagerUserAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.site_header = 'EnR Employee Management System'
