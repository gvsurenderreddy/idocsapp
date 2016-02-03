# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from geoposition.fields import GeopositionField
from localflavor.br.forms import BRPhoneNumberField
from localflavor.br.br_states import STATE_CHOICES