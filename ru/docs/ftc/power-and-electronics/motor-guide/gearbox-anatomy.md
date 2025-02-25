# Внутренности коробки передач

По сути, коробка передач — это просто сборник шестерен и корпус, который соединяет их. У коробки передач есть **выходное отношение**, то есть конечное передаточное отношение между входом мотора и выходным [валом](#shaft).

> **Термин**: Передаточное отношение
    Также известное как gear ratio. В любой системе передачи вращающего момента (обычно включающей моторы и [серво](#servo) в FTC™), передаточное отношение определяет как количество вращений на входе системы, так и количество вращений на выходе.
> 
> Например, мотор NeveRest 20 состоит из немодифицированного [мотора NeveRest](#neverest-motor) и планетарной коробки передач с передаточным отношением 20:1 (или, когда говорят, "20 к 1"). Это означает, что для того, чтобы выходной вал коробки передач совершил 1 вращение, входной вал мотора должен совершить 20 вращений. Передаточные отношения — это один из самых важных факторов при проектировании компонента передачи энергии.
>
> Любой мотор или сервопривод FTC имеет два свойства: скорость и крутящий момент (или вращающую силу). Эти два свойства обратно пропорциональны, то есть увеличение скорости уменьшает крутящий момент, и наоборот. Например, если вы хотите сделать механизм быстрее за счет уменьшения крутящего момента, удвоив скорость коробки передач 20:1, вы уменьшаете передаточное отношение в 2 раза. Поскольку 20, разделенное на 2, дает 10, новое желаемое отношение будет 10:1 (это называется увеличением передачи). Однако, если вы хотите удвоить крутящий момент, делая систему более мощной и надежной за счет скорости, вы увеличиваете передаточное отношение в 2 раза, получив отношение 40:1 (это называется уменьшением передачи).
>
> Наиболее распространенные способы увеличения или уменьшения передаточного отношения — это использование коробок передач, шестерен, звездочек и шкивов с ременным приводом, все из которых существуют в различных размерах.

В FTC коробки передач могут быть более распространены, чем вы думаете — каждый мотор имеет прикрепленную к нему коробку передач. Эти коробки передач бывают двух типов: шестеренные или планетарные. Ниже мы представляем подробный анализ каждого из этих типов коробок передач. **Для разъяснения, коробки передач ниже отделены от базового мотора.**


## Шестеренные коробки передач (Spur Gearboxes)

>**Термин**: Шестеренная коробка передач
Шестеренная коробка передач использует прямозубые шестерни, которые располагаются друг на друге. Снижение скорости достигается с помощью шестерен разного размера, расположенных на одной плоскости.

Шестеренные коробки передач представляют собой систему [передаточных отношений](#gear-reduction), часто соединенных для достижения большого составного отношения (например, 40:1). Каждое отдельное отношение имеет только две [шестерни](#gear) — одна может быть 8:1, другая — 5:1, но итоговое отношение будет 40:1. Эти коробки передач используются в серии NeveRest Classic от Andymark и в моторах серии 5201 от goBILDA, а также в [моторе REV HD Hex](#hd-hex-motor). Из-за особенностей конструкции этих коробок передач, при каждом уменьшении скорости в работе участвует только несколько зубьев каждой [шестерни](#gear), и эти зубья несут всю нагрузку коробки. Легко повредить шестеренную коробку передач при ударных нагрузках, и если одна [шестерня](#gear) ломается, вся коробка передач перестает работать.

> **Совет:** Использование шестеренных коробок передач для высоконагруженных приложений, таких как трансмиссии или манипуляторы, не рекомендуется. Вместо этого используйте планетарные коробки передач.

![Пример шестеренной коробки передач](https://dd8f408.webp.ee/spur-gearbox.jpg)

### Преимущества шестеренных коробок передач

- Обычно шестеренные коробки передач дешевле планетарных. Однако в FTC эта разница в цене часто минимальна. Шестеренная коробка передач 20:1 от REV стоит всего на $4 дешевле, чем планетарная 20:1.
- Шестеренные коробки передач от разных производителей не являются взаимозаменяемыми. Тем не менее, их можно сравнивать, и их характеристики практически одинаковы. Основное, что нужно учитывать, это **желаемое передаточное отношение, тип соединения с мотором и тип выходного вала**.

## Планетарные коробки передач

Планетарные коробки передач используют более сложную систему шестерен для достижения надежного снижения скорости в компактном пространстве. В автомобильной инженерии планетарные механизмы могут достигать нескольких разных передаточных отношений без изменения размера шестерен, но все планетарные коробки передач, которые вы встретите в FTC, обычно имеют одно передаточное отношение.

> **Термин**:
> Планетарная передача
>
> Планетарная передача состоит из центральной шестерни (солнечная шестерня), вокруг которой вращаются меньшие шестерни (планетарные шестерни). Внешнее кольцо содержит другие шестерни, удерживающие их на месте.

Планетарные коробки передач используются в серии Andymark Orbital, некоторых моторах REV HD Hex Planetary и UltraPlanetary, а также в широком ассортименте планетарных моторов от goBILDA. Кроме того, AndyMark продает несколько планетарных коробок передач на замену, таких как NeveRest Sport и 57 Sport. Как видно из графики ниже, в этих коробках передач на каждом этапе вовлечено больше зубьев, чем в шестеренных коробках.

![Схема планетарной коробки передач](https://dd8f408.webp.ee/planetary-gearbox.jpg)

### Преимущества планетарных коробок передач

- Зазор (backlash) ниже, чем у шестеренных коробок передач. Зазор — это зазор или потеря движения, вызванная промежутками между частями. Это можно легко объяснить, поставив колесо или шестерню на вал мотора и слегка повернув его. Деталь должна немного покачиваться без значительного приложения силы. Это происходит из-за того, что невозможно добиться идеального зацепления зубьев шестерен в коробке передач, и аналогичная ситуация наблюдается у [цепей](#chain) и [звездочек](#sprocket), а также при любом другом способе передачи энергии. Однако планетарные коробки передач имеют меньший зазор, поскольку в них меньше ступеней передачи.
- Эффективность лучше, чем у шестеренных коробок передач. Типичная двухступенчатая шестеренная коробка передач имеет эффективность около 85%, в то время как двухступенчатые планетарные коробки передач обычно имеют эффективность 94%.
- Нагрузочная способность выше у планетарных коробок передач. Это связано с тем, что на каждом этапе работает несколько зубьев, что распределяет нагрузку.

> **Совет:** Это означает, что планетарные коробки передач не ломаются так легко при высоких нагрузках, таких как трансмиссии.