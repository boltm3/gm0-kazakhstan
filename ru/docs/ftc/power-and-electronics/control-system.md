# Системы управления

Система управления FTC основана на "**Контроллере робота**" и "**Станции водителя**". **Контроллер робота** устанавливается на роботе. Он либо встроен в робот, либо подключен к специальным "хабам", которые в свою очередь соединяются с моторами, сервоприводами и сенсорами. **Контроллер робота** соединён с **Станцией водителя** через Wi-Fi или Wi-Fi Direct.

REV Robotics является единственным производителем законных компонентов системы управления FTC. **REV Expansion Hub** подключается к моторам, сервоприводам, сенсорам и **Контроллеру робота**. **REV Control Hub** имеет те же функции, что и Expansion Hub, но с встроенным **Контроллером робота**.

Дополнительную информацию о системе управления FTC можно найти ниже:

- [Официальная документация по системе управления на FTC Docs](https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/control_system_intro/The-FTC-Control-System.html)
- [Документация REV Control System](https://docs.revrobotics.com/duo-control/)
- [Официальное руководство по устранению неполадок](https://www.firstinspires.org/sites/default/files/uploads/resource_library/ftc/control-system-troubleshooting-guide.pdf)

Есть две возможные системы управления, которые могут быть использованы на роботе FTC:

- **REV Control Hub + REV Expansion Hub**
- **RC Phone + REV Expansion Hub(s)**

## REV Control Hub + REV Expansion Hub

!> **Внимание**: Очень важно обновить прошивку REV Expansion Hub до версии 1.8.2 или выше. Это обеспечит лучшую защиту от отключений и улучшит производительность программы. См. [документацию по обновлению прошивки REV Expansion Hub](https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware).

Это стандартная система управления для команд, только начинающих заниматься FTC.

**Control Hub** подключается к **Expansion Hub** через соединение RS-485 или через USB-A (со стороны Control Hub) к mini-USB (со стороны Expansion Hub). В любом случае необходимо правильно организовать кабельную разводку и защиту от натяжения кабелей.

Для получения дополнительной информации о настройке Control Hub и конфигурации робота, ознакомьтесь с [Руководством по настройке Control Hub от REV Robotics](https://docs.revrobotics.com/duo-control/control-hub-gs).

![Диаграмма системы управления Control Hub + Expansion Hub](https://dd8f408.webp.ee/ch-wiring-diagram.jpg)
*Изображение: Диаграмма системы управления Control Hub + Expansion Hub*

## RC Phone + REV Expansion Hub

!> **Внимание**: Очень важно обновить прошивку REV Expansion Hub до версии 1.8.2 или выше. Это обеспечит лучшую защиту от отключений и улучшит производительность программы. См. [документацию по обновлению прошивки REV Expansion Hub](https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware).

**Expansion Hub** подключается к **Телефону-Контроллеру** через мини-USB порт. **REV Expansion Hub** работает надежно, если правильно организовать защиту от натяжения кабелей. Это включает в себя использование **USB Retention Mount**, а также 3D-печать **XT30** креплений для защиты от натяжения кабелей.

Для получения дополнительной информации о настройке Expansion Hub и конфигурации робота, ознакомьтесь с [Руководством по настройке Expansion Hub от REV Robotics](https://docs.revrobotics.com/duo-control/legacy/expansion-hub-gs).

- [USB Retention Mount](https://www.revrobotics.com/rev-41-1214/)
- [XT30 Stress Relief](https://www.thingiverse.com/thing:2887045)

![Диаграмма системы управления RC Phone + Expansion Hub(s)](https://dd8f408.webp.ee/exh-wiring-diagram.jpg)