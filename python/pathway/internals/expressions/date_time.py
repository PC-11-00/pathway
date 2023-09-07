# Copyright © 2023 Pathway

from typing import Optional, Union

import pathway.internals.expression as expr
from pathway.internals import api
from pathway.internals.datetime_types import DateTimeNaive, DateTimeUtc, Duration


class DateTimeNamespace:
    """A module containing methods related to DateTimes.
    They can be called using a `dt` attribute of an expression.

    Typical use:

    >>> import pathway as pw
    >>> table = pw.debug.table_from_markdown(
    ...     '''
    ...      |         t1
    ...    1 | 2023-05-15T14:13:00
    ... '''
    ... )
    >>> table_with_datetime = table.select(t1=table.t1.dt.strptime("%Y-%m-%dT%H:%M:%S"))
    >>> table_with_days = table_with_datetime.select(day=table_with_datetime.t1.dt.day())
    """

    _expression: expr.ColumnExpression

    def __init__(self, expression: expr.ColumnExpression):
        self._expression = expression

    def nanosecond(self) -> expr.ColumnExpression:
        """Extracts nanoseconds from a DateTime.

        Returns:
            Nanosecond as int. 0 <= nanosecond < 1_000_000_000

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    1 | 2023-05-15T10:13:00.000000000
        ...    2 | 2023-05-15T10:13:00.000000012
        ...    3 | 2023-05-15T10:13:00.123456789
        ...    4 | 2023-05-15T10:13:23.123456789
        ... '''
        ... )
        >>> table_with_datetime = table.select(t1=table.t1.dt.strptime("%Y-%m-%dT%H:%M:%S.%f"))
        >>> table_with_nanoseconds = table_with_datetime.select(
        ...     nanosecond=table_with_datetime.t1.dt.nanosecond()
        ... )
        >>> pw.debug.compute_and_print(table_with_nanoseconds, include_id=False)
        nanosecond
        0
        12
        123456789
        123456789
        """

        return expr.MethodCallExpression(
            [
                (DateTimeNaive, int, api.Expression.date_time_naive_nanosecond),
                (DateTimeUtc, int, api.Expression.date_time_utc_nanosecond),
            ],
            "dt.nanosecond",
            self._expression,
        )

    def microsecond(self) -> expr.ColumnExpression:
        """Extracts microseconds from a DateTime.

        Returns:
            Microsecond as int. 0 <= microsecond < 1_000_000

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    1 | 2023-05-15T10:13:00.000000000
        ...    2 | 2023-05-15T10:13:00.000012000
        ...    3 | 2023-05-15T10:13:00.123456789
        ...    4 | 2023-05-15T10:13:23.123456789
        ... '''
        ... )
        >>> table_with_datetime = table.select(t1=table.t1.dt.strptime("%Y-%m-%dT%H:%M:%S.%f"))
        >>> table_with_microseconds = table_with_datetime.select(
        ...     microsecond=table_with_datetime.t1.dt.microsecond()
        ... )
        >>> pw.debug.compute_and_print(table_with_microseconds, include_id=False)
        microsecond
        0
        12
        123456
        123456
        """

        return expr.MethodCallExpression(
            [
                (DateTimeNaive, int, api.Expression.date_time_naive_microsecond),
                (DateTimeUtc, int, api.Expression.date_time_utc_microsecond),
            ],
            "dt.microsecond",
            self._expression,
        )

    def millisecond(self) -> expr.ColumnExpression:
        """Extracts milliseconds from a DateTime.

        Returns:
            Millisecond as int. 0 <= millisecond < 1_000

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    1 | 2023-05-15T10:13:00.000000000
        ...    2 | 2023-05-15T10:13:00.012000000
        ...    3 | 2023-05-15T10:13:00.123456789
        ...    4 | 2023-05-15T10:13:23.123456789
        ... '''
        ... )
        >>> table_with_datetime = table.select(t1=table.t1.dt.strptime("%Y-%m-%dT%H:%M:%S.%f"))
        >>> table_with_milliseconds = table_with_datetime.select(
        ...     millisecond=table_with_datetime.t1.dt.millisecond()
        ... )
        >>> pw.debug.compute_and_print(table_with_milliseconds, include_id=False)
        millisecond
        0
        12
        123
        123
        """

        return expr.MethodCallExpression(
            [
                (DateTimeNaive, int, api.Expression.date_time_naive_millisecond),
                (DateTimeUtc, int, api.Expression.date_time_utc_millisecond),
            ],
            "dt.millisecond",
            self._expression,
        )

    def second(self) -> expr.ColumnExpression:
        """Extracts seconds from a DateTime.

        Returns:
            Second as int. 0 <= second < 60

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    1 | 2023-05-15T10:13:00.000000000
        ...    2 | 2023-05-15T10:13:00.123456789
        ...    3 | 2023-05-15T10:13:23.000000000
        ...    4 | 2023-05-15T10:13:23.123456789
        ... '''
        ... )
        >>> table_with_datetime = table.select(t1=table.t1.dt.strptime("%Y-%m-%dT%H:%M:%S.%f"))
        >>> table_with_seconds = table_with_datetime.select(
        ...     second=table_with_datetime.t1.dt.second()
        ... )
        >>> pw.debug.compute_and_print(table_with_seconds, include_id=False)
        second
        0
        0
        23
        23
        """

        return expr.MethodCallExpression(
            [
                (DateTimeNaive, int, api.Expression.date_time_naive_second),
                (DateTimeUtc, int, api.Expression.date_time_utc_second),
            ],
            "dt.second",
            self._expression,
        )

    def minute(self) -> expr.ColumnExpression:
        """Extracts minute from a DateTime.

        Returns:
            Minute as int. 0 <= minute < 60

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    1 | 2023-05-15T10:00:00
        ...    2 | 2023-05-15T10:00:23
        ...    3 | 2023-05-15T10:13:00
        ...    4 | 2023-05-15T10:13:23
        ... '''
        ... )
        >>> table_with_datetime = table.select(t1=table.t1.dt.strptime("%Y-%m-%dT%H:%M:%S"))
        >>> table_with_minutes = table_with_datetime.select(
        ...     minute=table_with_datetime.t1.dt.minute()
        ... )
        >>> pw.debug.compute_and_print(table_with_minutes, include_id=False)
        minute
        0
        0
        13
        13
        """

        return expr.MethodCallExpression(
            [
                (DateTimeNaive, int, api.Expression.date_time_naive_minute),
                (DateTimeUtc, int, api.Expression.date_time_utc_minute),
            ],
            "dt.minute",
            self._expression,
        )

    def hour(self) -> expr.ColumnExpression:
        """Extracts hour from a DateTime.

        Returns:
            Hour as int. 0 <= hour < 24

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    1 | 2023-05-15T00:00:00
        ...    2 | 2023-05-15T12:00:00
        ...    3 | 2023-05-15T14:13:00
        ... '''
        ... )
        >>> table_with_datetime = table.select(t1=table.t1.dt.strptime("%Y-%m-%dT%H:%M:%S"))
        >>> table_with_hours = table_with_datetime.select(hour=table_with_datetime.t1.dt.hour())
        >>> pw.debug.compute_and_print(table_with_hours, include_id=False)
        hour
        0
        12
        14
        """

        return expr.MethodCallExpression(
            [
                (DateTimeNaive, int, api.Expression.date_time_naive_hour),
                (DateTimeUtc, int, api.Expression.date_time_utc_hour),
            ],
            "dt.hour",
            self._expression,
        )

    def day(self) -> expr.ColumnExpression:
        """Extracts day from a DateTime.

        Returns:
            Day as int. 1 <= day <= 31 (depending on a month)

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    1 | 1974-03-12T00:00:00
        ...    2 | 2023-03-25T12:00:00
        ...    3 | 2023-05-15T14:13:00
        ... '''
        ... )
        >>> table_with_datetime = table.select(t1=table.t1.dt.strptime("%Y-%m-%dT%H:%M:%S"))
        >>> table_with_days = table_with_datetime.select(day=table_with_datetime.t1.dt.day())
        >>> pw.debug.compute_and_print(table_with_days, include_id=False)
        day
        12
        15
        25
        """

        return expr.MethodCallExpression(
            [
                (DateTimeNaive, int, api.Expression.date_time_naive_day),
                (DateTimeUtc, int, api.Expression.date_time_utc_day),
            ],
            "dt.day",
            self._expression,
        )

    def month(self) -> expr.ColumnExpression:
        """Extracts month from a DateTime.

        Returns:
            Month as int. 1 <= month <= 12

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    1 | 1974-03-12T00:00:00
        ...    2 | 2023-03-25T12:00:00
        ...    3 | 2023-05-15T14:13:00
        ... '''
        ... )
        >>> table_with_datetime = table.select(t1=table.t1.dt.strptime("%Y-%m-%dT%H:%M:%S"))
        >>> table_with_months = table_with_datetime.select(month=table_with_datetime.t1.dt.month())
        >>> pw.debug.compute_and_print(table_with_months, include_id=False)
        month
        3
        3
        5
        """

        return expr.MethodCallExpression(
            [
                (DateTimeNaive, int, api.Expression.date_time_naive_month),
                (DateTimeUtc, int, api.Expression.date_time_utc_month),
            ],
            "dt.month",
            self._expression,
        )

    def year(self) -> expr.ColumnExpression:
        """Extracts year from a DateTime.

        Returns:
            Year as int.

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    1 | 1974-03-12T00:00:00
        ...    2 | 2023-03-25T12:00:00
        ...    3 | 2023-05-15T14:13:00
        ... '''
        ... )
        >>> table_with_datetime = table.select(t1=table.t1.dt.strptime("%Y-%m-%dT%H:%M:%S"))
        >>> table_with_years = table_with_datetime.select(year=table_with_datetime.t1.dt.year())
        >>> pw.debug.compute_and_print(table_with_years, include_id=False)
        year
        1974
        2023
        2023
        """

        return expr.MethodCallExpression(
            [
                (DateTimeNaive, int, api.Expression.date_time_naive_year),
                (DateTimeUtc, int, api.Expression.date_time_utc_year),
            ],
            "dt.year",
            self._expression,
        )

    def timestamp(self) -> expr.ColumnExpression:
        """Returns a number of nanoseconds from 1970-01-01 for naive DateTime
        and from 1970-01-01 UTC for timezone-aware datetime.

        Returns:
            Timestamp as int.

        Examples:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    0 | 1969-01-01T00:00:00.000000000
        ...    1 | 1970-01-01T00:00:00.000000000
        ...    2 | 2023-01-01T00:00:00.000000000
        ...    3 | 2023-03-25T00:00:00.000000000
        ...    4 | 2023-03-25T13:45:26.000000000
        ...    5 | 2023-03-25T13:45:26.987654321
        ... '''
        ... )
        >>> table_with_datetime = table.select(t1=table.t1.dt.strptime("%Y-%m-%dT%H:%M:%S.%f"))
        >>> table_with_timestamp = table_with_datetime.select(
        ...     timestamp=table_with_datetime.t1.dt.timestamp()
        ... )
        >>> pw.debug.compute_and_print(table_with_timestamp, include_id=False)
        timestamp
        -31536000000000000
        0
        1672531200000000000
        1679702400000000000
        1679751926000000000
        1679751926987654321
        >>>
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    1 | 1969-01-01T00:00:00.000000000+00:00
        ...    2 | 1970-01-01T00:00:00.000000000+00:00
        ...    3 | 1970-01-01T00:00:00.000000000+02:00
        ...    4 | 1970-01-01T00:00:00.000000000-03:00
        ...    5 | 2023-01-01T00:00:00.000000000+01:00
        ...    6 | 2023-03-25T00:00:00.000000000+01:00
        ...    7 | 2023-03-25T13:45:26.000000000+01:00
        ...    8 | 2023-03-25T13:45:26.987654321+01:00
        ... '''
        ... )
        >>> table_with_datetime = table.select(t1=table.t1.dt.strptime("%Y-%m-%dT%H:%M:%S.%f%z"))
        >>> table_with_timestamp = table_with_datetime.select(
        ...     timestamp=table_with_datetime.t1.dt.timestamp()
        ... )
        >>> pw.debug.compute_and_print(table_with_timestamp, include_id=False)
        timestamp
        -31536000000000000
        -7200000000000
        0
        10800000000000
        1672527600000000000
        1679698800000000000
        1679748326000000000
        1679748326987654321
        """

        return expr.MethodCallExpression(
            [
                (DateTimeNaive, int, api.Expression.date_time_naive_timestamp),
                (DateTimeUtc, int, api.Expression.date_time_utc_timestamp),
            ],
            "dt.timestamp",
            self._expression,
        )

    def strftime(self, fmt: Union[expr.ColumnExpression, str]) -> expr.ColumnExpression:
        """Converts a DateTime to a string.

        Args:
            fmt: Format string. We use the specifiers of \
            `chrono <https://docs.rs/chrono/latest/chrono/format/strftime/index.html>`_ \
            library. In most cases they are identical to standard python specifiers in \
            `strftime <https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior>`_ .

        Returns:
            str

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    1 | 1970-02-03T10:13:00
        ...    2 | 2023-03-25T10:13:00
        ...    3 | 2023-03-26T12:13:00
        ...    4 | 2023-05-15T14:13:23
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S"
        >>> table_with_datetime = table.select(t1=pw.this.t1.dt.strptime(fmt=fmt))
        >>> table_formatted = table_with_datetime.select(
        ...     date=pw.this.t1.dt.strftime("%d.%m.%Y"),
        ...     full_date=pw.this.t1.dt.strftime("%B %d, %Y"),
        ...     time_24=pw.this.t1.dt.strftime("%H:%M:%S"),
        ...     time_12=pw.this.t1.dt.strftime("%I:%M:%S %p"),
        ... )
        >>> pw.debug.compute_and_print(table_formatted, include_id=False)
        date       | full_date         | time_24  | time_12
        03.02.1970 | February 03, 1970 | 10:13:00 | 10:13:00 AM
        15.05.2023 | May 15, 2023      | 14:13:23 | 02:13:23 PM
        25.03.2023 | March 25, 2023    | 10:13:00 | 10:13:00 AM
        26.03.2023 | March 26, 2023    | 12:13:00 | 12:13:00 PM
        """

        return expr.MethodCallExpression(
            [
                ((DateTimeNaive, str), str, api.Expression.date_time_naive_strftime),
                ((DateTimeUtc, str), str, api.Expression.date_time_utc_strftime),
            ],
            "dt.strftime",
            self._expression,
            fmt,
        )

    def strptime(
        self,
        fmt: Union[expr.ColumnExpression, str],
        contains_timezone: Optional[bool] = None,
    ) -> expr.ColumnExpression:
        """Converts a string to a DateTime. If the string contains a timezone and
        a %z specifier is used, timezone-aware DateTime is created.
        Then the timezone is converted to a server timezone (see examples).
        If the string contains no timezone, a naive (not aware of timezone) DateTime
        is created.

        Args:
            fmt: Format string. We use the specifiers of \
            `chrono <https://docs.rs/chrono/latest/chrono/format/strftime/index.html>`_ \
            library. In most cases they are identical to standard python specifiers in \
            `strptime <https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior>`_ . \
            contains_timezone: If fmt is not a single string (the same for all objects) \
            but a ColumnExpression, you need to set this parameter so that the function \
            can determine if the return type is `DateTimeNaive` (`contains_timezone = False`) \
            or `DateTimeUtc` (`contains_timezone = True`).

        Returns:
            DateTime

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    1 | 1970-02-03T10:13:00.000000000
        ...    2 | 2023-03-25T10:13:00.000000012
        ...    3 | 2023-03-26T12:13:00.123456789
        ...    4 | 2023-05-15T14:13:23.123456789
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S.%f"
        >>> table_with_datetime = table.select(t1=table.t1.dt.strptime(fmt=fmt))
        >>> pw.debug.compute_and_print(table_with_datetime, include_id=False)
        t1
        1970-02-03 10:13:00
        2023-03-25 10:13:00.000000012
        2023-03-26 12:13:00.123456789
        2023-05-15 14:13:23.123456789
        >>>
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    1 | 03.02.1970T10:13:00.000000000
        ...    2 | 25.03.2023T10:13:00.000000012
        ...    3 | 26.03.2023T12:13:00.123456789
        ...    4 | 15.05.2023T14:13:23.123456789
        ... '''
        ... )
        >>> fmt = "%d.%m.%YT%H:%M:%S.%f"
        >>> table_with_datetime = table.select(t1=table.t1.dt.strptime(fmt=fmt))
        >>> pw.debug.compute_and_print(table_with_datetime, include_id=False)
        t1
        1970-02-03 10:13:00
        2023-03-25 10:13:00.000000012
        2023-03-26 12:13:00.123456789
        2023-05-15 14:13:23.123456789
        >>>
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1
        ...    1 | 1970-02-03T10:13:00-02:00
        ...    2 | 2023-03-25T10:13:00+00:00
        ...    3 | 2023-03-26T12:13:00-01:00
        ...    4 | 2023-05-15T14:13:23+00:30
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S%z"
        >>> table_with_datetime = table.select(t1=table.t1.dt.strptime(fmt=fmt))
        >>> pw.debug.compute_and_print(table_with_datetime, include_id=False)
        t1
        1970-02-03 12:13:00+00:00
        2023-03-25 10:13:00+00:00
        2023-03-26 13:13:00+00:00
        2023-05-15 13:43:23+00:00
        """

        if contains_timezone is None:
            if isinstance(fmt, str):
                contains_timezone = "%z" in fmt or "%Z" in fmt
            else:
                raise ValueError(
                    "If fmt is not a string, you need to specify whether objects"
                    + " contain a timezone using `contains_timezone` parameter."
                )

        if contains_timezone:
            fun = api.Expression.date_time_utc_strptime
            return_type: type = DateTimeUtc
        else:
            fun = api.Expression.date_time_naive_strptime
            return_type = DateTimeNaive

        return expr.MethodCallExpression(
            [((str, str), return_type, fun)],
            "dt.strptime",
            self._expression,
            fmt,
        )

    def to_utc(
        self, from_timezone: Union[expr.ColumnExpression, str]
    ) -> expr.ColumnExpression:
        """Converts DateTimeNaive to UTC from time zone provided as `from_timezone`
        argument. If the given DateTime doesn't exist in the provided time zone it is
        mapped to the first existing DateTime after it. If a given DateTime corresponds
        to more than one moments in the provided time zone, it is mapped to a later
        moment.

        Args:
            from_timezone: The time zone to convert from.

        Returns:
            DateTimeUtc

        Examples:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |         date
        ...    1 | 2023-03-26T01:59:00
        ...    2 | 2023-03-26T02:30:00
        ...    3 | 2023-03-26T03:00:00
        ...    4 | 2023-03-27T01:59:00
        ...    5 | 2023-03-27T02:30:00
        ...    6 | 2023-03-27T03:00:00
        ...    7 | 2023-10-29T01:59:00
        ...    8 | 2023-10-29T02:00:00
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S"
        >>> table_local = table.select(date=pw.this.date.dt.strptime(fmt=fmt))
        >>> table_utc = table_local.with_columns(
        ...     date_utc=pw.this.date.dt.to_utc(from_timezone="Europe/Warsaw"),
        ... )
        >>> pw.debug.compute_and_print(table_utc, include_id=False)
        date                | date_utc
        2023-03-26 01:59:00 | 2023-03-26 00:59:00+00:00
        2023-03-26 02:30:00 | 2023-03-26 01:00:00+00:00
        2023-03-26 03:00:00 | 2023-03-26 01:00:00+00:00
        2023-03-27 01:59:00 | 2023-03-26 23:59:00+00:00
        2023-03-27 02:30:00 | 2023-03-27 00:30:00+00:00
        2023-03-27 03:00:00 | 2023-03-27 01:00:00+00:00
        2023-10-29 01:59:00 | 2023-10-28 23:59:00+00:00
        2023-10-29 02:00:00 | 2023-10-29 01:00:00+00:00
        >>>
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |         date
        ...    1 | 2023-03-12T01:59:00
        ...    2 | 2023-03-12T02:30:00
        ...    3 | 2023-03-12T03:00:00
        ...    4 | 2023-03-13T01:59:00
        ...    5 | 2023-03-13T02:30:00
        ...    6 | 2023-03-13T03:00:00
        ...    7 | 2023-11-05T00:59:00
        ...    8 | 2023-11-05T01:00:00
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S"
        >>> table_local = table.select(date=pw.this.date.dt.strptime(fmt=fmt))
        >>> table_utc = table_local.with_columns(
        ...     date_utc=pw.this.date.dt.to_utc(from_timezone="America/Los_Angeles"),
        ... )
        >>> pw.debug.compute_and_print(table_utc, include_id=False)
        date                | date_utc
        2023-03-12 01:59:00 | 2023-03-12 09:59:00+00:00
        2023-03-12 02:30:00 | 2023-03-12 10:00:00+00:00
        2023-03-12 03:00:00 | 2023-03-12 10:00:00+00:00
        2023-03-13 01:59:00 | 2023-03-13 08:59:00+00:00
        2023-03-13 02:30:00 | 2023-03-13 09:30:00+00:00
        2023-03-13 03:00:00 | 2023-03-13 10:00:00+00:00
        2023-11-05 00:59:00 | 2023-11-05 07:59:00+00:00
        2023-11-05 01:00:00 | 2023-11-05 09:00:00+00:00
        """

        return expr.MethodCallExpression(
            [
                (
                    (DateTimeNaive, str),
                    DateTimeUtc,
                    api.Expression.date_time_naive_to_utc,
                ),
            ],
            "dt.to_utc",
            self._expression,
            from_timezone,
        )

    def to_naive_in_timezone(
        self, timezone: Union[expr.ColumnExpression, str]
    ) -> expr.ColumnExpression:
        """Converts DateTimeUtc to time zone specified as `timezone` argument.

        Args:
            timezone: The time zone to convert to.

        Returns:
            DateTimeNaive

        Examples:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |        date_utc
        ...    1 | 2023-03-26T00:59:00+00:00
        ...    2 | 2023-03-26T01:00:00+00:00
        ...    3 | 2023-03-27T00:59:00+00:00
        ...    4 | 2023-03-27T01:00:00+00:00
        ...    5 | 2023-10-28T23:59:00+00:00
        ...    6 | 2023-10-29T00:00:00+00:00
        ...    7 | 2023-10-29T00:30:00+00:00
        ...    8 | 2023-10-29T01:00:00+00:00
        ...    9 | 2023-10-29T01:30:00+00:00
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S%z"
        >>> table_utc = table.select(date_utc=pw.this.date_utc.dt.strptime(fmt=fmt))
        >>> table_local = table_utc.with_columns(
        ...     date=pw.this.date_utc.dt.to_naive_in_timezone(timezone="Europe/Warsaw"),
        ... )
        >>> pw.debug.compute_and_print(table_local, include_id=False)
        date_utc                  | date
        2023-03-26 00:59:00+00:00 | 2023-03-26 01:59:00
        2023-03-26 01:00:00+00:00 | 2023-03-26 03:00:00
        2023-03-27 00:59:00+00:00 | 2023-03-27 02:59:00
        2023-03-27 01:00:00+00:00 | 2023-03-27 03:00:00
        2023-10-28 23:59:00+00:00 | 2023-10-29 01:59:00
        2023-10-29 00:00:00+00:00 | 2023-10-29 02:00:00
        2023-10-29 00:30:00+00:00 | 2023-10-29 02:30:00
        2023-10-29 01:00:00+00:00 | 2023-10-29 02:00:00
        2023-10-29 01:30:00+00:00 | 2023-10-29 02:30:00
        >>>
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |        date_utc
        ...    1 | 2023-03-12T09:59:00+00:00
        ...    2 | 2023-03-12T10:00:00+00:00
        ...    3 | 2023-03-13T09:59:00+00:00
        ...    4 | 2023-03-13T10:00:00+00:00
        ...    5 | 2023-11-05T07:59:00+00:00
        ...    6 | 2023-11-05T08:00:00+00:00
        ...    7 | 2023-11-05T08:30:00+00:00
        ...    8 | 2023-11-05T09:00:00+00:00
        ...    9 | 2023-11-05T09:30:00+00:00
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S%z"
        >>> table_utc = table.select(date_utc=pw.this.date_utc.dt.strptime(fmt=fmt))
        >>> table_local = table_utc.with_columns(
        ...     date=pw.this.date_utc.dt.to_naive_in_timezone(timezone="America/Los_Angeles"),
        ... )
        >>> pw.debug.compute_and_print(table_local, include_id=False)
        date_utc                  | date
        2023-03-12 09:59:00+00:00 | 2023-03-12 01:59:00
        2023-03-12 10:00:00+00:00 | 2023-03-12 03:00:00
        2023-03-13 09:59:00+00:00 | 2023-03-13 02:59:00
        2023-03-13 10:00:00+00:00 | 2023-03-13 03:00:00
        2023-11-05 07:59:00+00:00 | 2023-11-05 00:59:00
        2023-11-05 08:00:00+00:00 | 2023-11-05 01:00:00
        2023-11-05 08:30:00+00:00 | 2023-11-05 01:30:00
        2023-11-05 09:00:00+00:00 | 2023-11-05 01:00:00
        2023-11-05 09:30:00+00:00 | 2023-11-05 01:30:00
        """

        return expr.MethodCallExpression(
            [
                (
                    (DateTimeUtc, str),
                    DateTimeNaive,
                    api.Expression.date_time_utc_to_naive,
                ),
            ],
            "dt.to_to_naive_in_timezone",
            self._expression,
            timezone,
        )

    def add_duration_in_timezone(
        self,
        duration: Union[expr.ColumnExpression, Duration],
        timezone: Union[expr.ColumnExpression, str],
    ) -> expr.ColumnExpression:
        """Adds Duration to DateTime taking into account time zone.

        Args:
            duration: Duration to be added to DateTime.
            timezone: The time zone to perform addition in.

        Returns:
            DateTimeNaive or DateTimeUtc depending on the type of an object \
                the method was called on

        Example:

        >>> import pathway as pw
        >>> import datetime
        >>> t1 = pw.debug.table_from_markdown(
        ...     '''
        ...      |        date
        ...    1 | 2023-03-26T01:23:00
        ...    2 | 2023-03-27T01:23:00
        ...    3 | 2023-10-29T01:23:00
        ...    4 | 2023-10-30T01:23:00
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S"
        >>> t2 = t1.select(date=pw.this.date.dt.strptime(fmt=fmt))
        >>> t3 = t2.with_columns(
        ...     new_date=pw.this.date.dt.add_duration_in_timezone(
        ...         datetime.timedelta(hours=2), timezone="Europe/Warsaw"
        ...     ),
        ... )
        >>> pw.debug.compute_and_print(t3, include_id=False)
        date                | new_date
        2023-03-26 01:23:00 | 2023-03-26 04:23:00
        2023-03-27 01:23:00 | 2023-03-27 03:23:00
        2023-10-29 01:23:00 | 2023-10-29 02:23:00
        2023-10-30 01:23:00 | 2023-10-30 03:23:00
        """

        return (self.to_utc(timezone) + duration).dt.to_naive_in_timezone(timezone)

    def subtract_duration_in_timezone(
        self,
        duration: Union[expr.ColumnExpression, Duration],
        timezone: Union[expr.ColumnExpression, str],
    ) -> expr.ColumnExpression:
        """Subtracts Duration from DateTime taking into account time zone.

        Args:
            duration: Duration to be subtracted from DateTime.
            timezone: The time zone to perform subtraction in.

        Returns:
            DateTimeNaive or DateTimeUtc depending on the type of an object \
                the method was called on

        Example:

        >>> import pathway as pw
        >>> import datetime
        >>> t1 = pw.debug.table_from_markdown(
        ...     '''
        ...      |        date
        ...    1 | 2023-03-26T03:23:00
        ...    2 | 2023-03-27T03:23:00
        ...    3 | 2023-10-29T03:23:00
        ...    4 | 2023-10-30T03:23:00
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S"
        >>> t2 = t1.select(date=pw.this.date.dt.strptime(fmt=fmt))
        >>> t3 = t2.with_columns(
        ...     new_date=pw.this.date.dt.subtract_duration_in_timezone(
        ...         datetime.timedelta(hours=2), timezone="Europe/Warsaw"
        ...     ),
        ... )
        >>> pw.debug.compute_and_print(t3, include_id=False)
        date                | new_date
        2023-03-26 03:23:00 | 2023-03-26 00:23:00
        2023-03-27 03:23:00 | 2023-03-27 01:23:00
        2023-10-29 03:23:00 | 2023-10-29 02:23:00
        2023-10-30 03:23:00 | 2023-10-30 01:23:00
        """

        return (self.to_utc(timezone) - duration).dt.to_naive_in_timezone(timezone)

    def subtract_date_time_in_timezone(
        self,
        date_time: Union[expr.ColumnExpression, DateTimeNaive],
        timezone: Union[expr.ColumnExpression, str],
    ) -> expr.ColumnBinaryOpExpression:
        """Subtracts two DateTimeNaives taking into account time zone.

        Args:
            date_time: DateTimeNaive to be subtracted from `self`.
            timezone: The time zone to perform subtraction in.

        Returns:
            Duration

        Example:

        >>> import pathway as pw
        >>> t1 = pw.debug.table_from_markdown(
        ...     '''
        ...      |        date1        |        date2
        ...    1 | 2023-03-26T03:20:00 | 2023-03-26T01:20:00
        ...    2 | 2023-03-27T03:20:00 | 2023-03-27T01:20:00
        ...    3 | 2023-10-29T03:20:00 | 2023-10-29T01:20:00
        ...    4 | 2023-10-30T03:20:00 | 2023-10-30T01:20:00
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S"
        >>> t2 = t1.select(
        ...     date1=pw.this.date1.dt.strptime(fmt=fmt), date2=pw.this.date2.dt.strptime(fmt=fmt)
        ... )
        >>> t3 = t2.with_columns(
        ...     diff=pw.this.date1.dt.subtract_date_time_in_timezone(
        ...         pw.this.date2, timezone="Europe/Warsaw"
        ...     ),
        ... )
        >>> pw.debug.compute_and_print(t3, include_id=False)
        date1               | date2               | diff
        2023-03-26 03:20:00 | 2023-03-26 01:20:00 | 0 days 01:00:00
        2023-03-27 03:20:00 | 2023-03-27 01:20:00 | 0 days 02:00:00
        2023-10-29 03:20:00 | 2023-10-29 01:20:00 | 0 days 03:00:00
        2023-10-30 03:20:00 | 2023-10-30 01:20:00 | 0 days 02:00:00
        """

        return self.to_utc(timezone) - expr._wrap_arg(date_time).dt.to_utc(timezone)

    def round(
        self, duration: Union[expr.ColumnExpression, Duration]
    ) -> expr.ColumnExpression:
        """Rounds DateTime to precision specified by `duration` argument.

        Args:
            duration: rounding precision

        Returns:
            DateTimeNaive or DateTimeUtc depending on the type of an object \
                the method was called on

        Examples:

        >>> import pathway as pw
        >>> import datetime
        >>> t1 = pw.debug.table_from_markdown(
        ...     '''
        ...      |         date
        ...    1 | 2023-05-15T12:23:12
        ...    2 | 2023-05-15T12:33:21
        ...    3 | 2023-05-15T13:20:35
        ...    4 | 2023-05-15T13:51:41
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S"
        >>> t2 = t1.select(date=pw.this.date.dt.strptime(fmt=fmt))
        >>> res = t2.with_columns(
        ...     rounded_to_hours=pw.this.date.dt.round(datetime.timedelta(hours=1)),
        ...     rounded_to_10_min=pw.this.date.dt.round(datetime.timedelta(minutes=10)),
        ...     rounded_to_15_s=pw.this.date.dt.round(datetime.timedelta(seconds=15)),
        ... )
        >>> pw.debug.compute_and_print(res, include_id=False)
        date                | rounded_to_hours    | rounded_to_10_min   | rounded_to_15_s
        2023-05-15 12:23:12 | 2023-05-15 12:00:00 | 2023-05-15 12:20:00 | 2023-05-15 12:23:15
        2023-05-15 12:33:21 | 2023-05-15 13:00:00 | 2023-05-15 12:30:00 | 2023-05-15 12:33:15
        2023-05-15 13:20:35 | 2023-05-15 13:00:00 | 2023-05-15 13:20:00 | 2023-05-15 13:20:30
        2023-05-15 13:51:41 | 2023-05-15 14:00:00 | 2023-05-15 13:50:00 | 2023-05-15 13:51:45
        """

        return expr.MethodCallExpression(
            [
                (
                    (DateTimeNaive, Duration),
                    DateTimeNaive,
                    api.Expression.date_time_naive_round,
                ),
                (
                    (DateTimeUtc, Duration),
                    DateTimeUtc,
                    api.Expression.date_time_utc_round,
                ),
            ],
            "dt.round",
            self._expression,
            duration,
        )

    def floor(
        self, duration: Union[expr.ColumnExpression, Duration]
    ) -> expr.ColumnExpression:
        """Truncates DateTime to precision specified by `duration` argument.

        Args:
            duration: truncation precision

        Returns:
            DateTimeNaive or DateTimeUtc depending on the type of an object \
                the method was called on

        Examples:

        >>> import pathway as pw
        >>> import datetime
        >>> t1 = pw.debug.table_from_markdown(
        ...     '''
        ...      |         date
        ...    1 | 2023-05-15T12:23:12
        ...    2 | 2023-05-15T12:33:21
        ...    3 | 2023-05-15T13:20:35
        ...    4 | 2023-05-15T13:51:41
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S"
        >>> t2 = t1.select(date=pw.this.date.dt.strptime(fmt=fmt))
        >>> res = t2.with_columns(
        ...     truncated_to_hours=pw.this.date.dt.floor(datetime.timedelta(hours=1)),
        ...     truncated_to_10_min=pw.this.date.dt.floor(datetime.timedelta(minutes=10)),
        ...     truncated_to_15_s=pw.this.date.dt.floor(datetime.timedelta(seconds=15)),
        ... )
        >>> pw.debug.compute_and_print(res, include_id=False)
        date                | truncated_to_hours  | truncated_to_10_min | truncated_to_15_s
        2023-05-15 12:23:12 | 2023-05-15 12:00:00 | 2023-05-15 12:20:00 | 2023-05-15 12:23:00
        2023-05-15 12:33:21 | 2023-05-15 12:00:00 | 2023-05-15 12:30:00 | 2023-05-15 12:33:15
        2023-05-15 13:20:35 | 2023-05-15 13:00:00 | 2023-05-15 13:20:00 | 2023-05-15 13:20:30
        2023-05-15 13:51:41 | 2023-05-15 13:00:00 | 2023-05-15 13:50:00 | 2023-05-15 13:51:30
        """

        return expr.MethodCallExpression(
            [
                (
                    (DateTimeNaive, Duration),
                    DateTimeNaive,
                    api.Expression.date_time_naive_floor,
                ),
                (
                    (DateTimeUtc, Duration),
                    DateTimeUtc,
                    api.Expression.date_time_utc_floor,
                ),
            ],
            "dt.floor",
            self._expression,
            duration,
        )

    def nanoseconds(self) -> expr.ColumnExpression:
        """The total number of nanoseconds in a Duration.

        Returns:
            Nanoseconds as int.

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1              |               t2
        ...    0 | 2023-05-15T10:13:00.000000000 | 2023-05-15T10:13:23.123456789
        ...    1 | 2023-05-15T10:13:00.000000000 | 2023-05-15T10:13:00.000000000
        ...    2 | 2023-05-15T10:13:00.000000012 | 2023-05-15T10:13:00.000000000
        ...    3 | 2023-05-15T10:13:00.123456789 | 2023-05-15T10:13:00.000000000
        ...    4 | 2023-05-15T10:13:23.123456789 | 2023-05-15T10:13:00.000000000
        ...    5 | 2023-05-16T10:13:23.123456789 | 2023-05-15T10:13:00.000000000
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S.%f"
        >>> table_with_datetimes = table.select(
        ...     t1=pw.this.t1.dt.strptime(fmt=fmt), t2=pw.this.t2.dt.strptime(fmt=fmt)
        ... )
        >>> table_with_diff = table_with_datetimes.select(diff=pw.this.t1 - pw.this.t2)
        >>> table_with_nanoseconds = table_with_diff.select(
        ...     nanoseconds=pw.this["diff"].dt.nanoseconds()
        ... )
        >>> pw.debug.compute_and_print(table_with_nanoseconds, include_id=False)
        nanoseconds
        -23123456789
        0
        12
        123456789
        23123456789
        86423123456789
        """

        return expr.MethodCallExpression(
            [(Duration, int, api.Expression.duration_nanoseconds)],
            "dt.nanoseconds",
            self._expression,
        )

    def microseconds(self) -> expr.ColumnExpression:
        """The total number of microseconds in a Duration.

        Returns:
            Microseconds as int.

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1              |               t2
        ...    0 | 2023-05-15T10:13:00.000000000 | 2023-05-15T10:13:23.123456789
        ...    1 | 2023-05-15T10:13:00.000000000 | 2023-05-15T10:13:00.000000000
        ...    2 | 2023-05-15T10:13:00.000012000 | 2023-05-15T10:13:00.000000000
        ...    3 | 2023-05-15T10:13:00.123456789 | 2023-05-15T10:13:00.000000000
        ...    4 | 2023-05-15T10:13:23.123456789 | 2023-05-15T10:13:00.000000000
        ...    5 | 2023-05-16T10:13:23.123456789 | 2023-05-15T10:13:00.000000000
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S.%f"
        >>> table_with_datetimes = table.select(
        ...     t1=pw.this.t1.dt.strptime(fmt=fmt), t2=pw.this.t2.dt.strptime(fmt=fmt)
        ... )
        >>> table_with_diff = table_with_datetimes.select(diff=pw.this.t1 - pw.this.t2)
        >>> table_with_microseconds = table_with_diff.select(
        ...     microseconds=pw.this["diff"].dt.microseconds()
        ... )
        >>> pw.debug.compute_and_print(table_with_microseconds, include_id=False)
        microseconds
        -23123456
        0
        12
        123456
        23123456
        86423123456
        """

        return expr.MethodCallExpression(
            [(Duration, int, api.Expression.duration_microseconds)],
            "dt.microseconds",
            self._expression,
        )

    def milliseconds(self) -> expr.ColumnExpression:
        """The total number of milliseconds in a Duration.

        Returns:
            Milliseconds as int.

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1              |               t2
        ...    0 | 2023-05-15T10:13:00.000000000 | 2023-05-15T10:13:23.123456789
        ...    1 | 2023-05-15T10:13:00.000000000 | 2023-05-15T10:13:00.000000000
        ...    2 | 2023-05-15T10:13:00.012000000 | 2023-05-15T10:13:00.000000000
        ...    3 | 2023-05-15T10:13:00.123456789 | 2023-05-15T10:13:00.000000000
        ...    4 | 2023-05-15T10:13:23.123456789 | 2023-05-15T10:13:00.000000000
        ...    5 | 2023-05-16T10:13:23.123456789 | 2023-05-15T10:13:00.000000000
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S.%f"
        >>> table_with_datetimes = table.select(
        ...     t1=pw.this.t1.dt.strptime(fmt=fmt), t2=pw.this.t2.dt.strptime(fmt=fmt)
        ... )
        >>> table_with_diff = table_with_datetimes.select(diff=pw.this.t1 - pw.this.t2)
        >>> table_with_milliseconds = table_with_diff.select(
        ...     milliseconds=pw.this["diff"].dt.milliseconds()
        ... )
        >>> pw.debug.compute_and_print(table_with_milliseconds, include_id=False)
        milliseconds
        -23123
        0
        12
        123
        23123
        86423123
        """

        return expr.MethodCallExpression(
            [(Duration, int, api.Expression.duration_milliseconds)],
            "dt.milliseconds",
            self._expression,
        )

    def seconds(self) -> expr.ColumnExpression:
        """The total number of seconds in a Duration.

        Returns:
            Seconds as int.

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |               t1              |               t2
        ...    0 | 2023-05-15T10:13:00.000000000 | 2023-05-15T10:13:23.123456789
        ...    1 | 2023-05-15T10:13:00.000000000 | 2023-05-15T10:13:00.000000000
        ...    2 | 2023-05-15T10:13:00.123456789 | 2023-05-15T10:13:00.000000000
        ...    3 | 2023-05-15T10:13:23.000000000 | 2023-05-15T10:13:00.000000000
        ...    4 | 2023-05-15T10:13:23.123456789 | 2023-05-15T10:13:00.000000000
        ...    5 | 2023-05-16T10:13:23.123456789 | 2023-05-15T10:13:00.000000000
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S.%f"
        >>> table_with_datetimes = table.select(
        ...     t1=pw.this.t1.dt.strptime(fmt=fmt), t2=pw.this.t2.dt.strptime(fmt=fmt)
        ... )
        >>> table_with_diff = table_with_datetimes.select(diff=pw.this.t1 - pw.this.t2)
        >>> table_with_seconds = table_with_diff.select(seconds=pw.this["diff"].dt.seconds())
        >>> pw.debug.compute_and_print(table_with_seconds, include_id=False)
        seconds
        -23
        0
        0
        23
        23
        86423
        """

        return expr.MethodCallExpression(
            [(Duration, int, api.Expression.duration_seconds)],
            "dt.seconds",
            self._expression,
        )

    def minutes(self) -> expr.ColumnExpression:
        """The total number of minutes in a Duration.

        Returns:
            Minutes as int.

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |         t1          |         t2
        ...    0 | 2023-05-15T10:00:00 | 2023-05-15T10:13:23
        ...    1 | 2023-05-15T10:00:00 | 2023-05-15T10:00:00
        ...    2 | 2023-05-15T10:00:23 | 2023-05-15T10:00:00
        ...    3 | 2023-05-15T10:13:00 | 2023-05-15T10:00:00
        ...    4 | 2023-05-15T10:13:23 | 2023-05-15T10:00:00
        ...    5 | 2023-05-16T10:13:23 | 2023-05-15T10:00:00
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S"
        >>> table_with_datetimes = table.select(
        ...     t1=pw.this.t1.dt.strptime(fmt=fmt), t2=pw.this.t2.dt.strptime(fmt=fmt)
        ... )
        >>> table_with_diff = table_with_datetimes.select(diff=pw.this.t1 - pw.this.t2)
        >>> table_with_minutes = table_with_diff.select(minutes=pw.this["diff"].dt.minutes())
        >>> pw.debug.compute_and_print(table_with_minutes, include_id=False)
        minutes
        -13
        0
        0
        13
        13
        1453
        """

        return expr.MethodCallExpression(
            [(Duration, int, api.Expression.duration_minutes)],
            "dt.minutes",
            self._expression,
        )

    def hours(self) -> expr.ColumnExpression:
        """The total number of hours in a Duration.

        Returns:
            Hours as int.

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |         t1          |         t2
        ...    0 | 2023-05-15T00:00:00 | 2023-05-15T10:13:23
        ...    1 | 2023-05-15T00:00:00 | 2023-05-15T10:00:00
        ...    2 | 2023-05-15T10:00:00 | 2023-05-15T10:00:00
        ...    3 | 2023-05-15T10:00:23 | 2023-05-15T10:00:00
        ...    4 | 2023-05-15T12:13:00 | 2023-05-15T10:00:00
        ...    5 | 2023-05-15T14:13:23 | 2023-05-15T10:00:00
        ...    6 | 2023-05-16T10:13:23 | 2023-05-15T10:00:00
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S"
        >>> table_with_datetimes = table.select(
        ...     t1=pw.this.t1.dt.strptime(fmt=fmt), t2=pw.this.t2.dt.strptime(fmt=fmt)
        ... )
        >>> table_with_diff = table_with_datetimes.select(diff=pw.this.t1 - pw.this.t2)
        >>> table_with_hours = table_with_diff.select(hours=pw.this["diff"].dt.hours())
        >>> pw.debug.compute_and_print(table_with_hours, include_id=False)
        hours
        -10
        -10
        0
        0
        2
        4
        24
        """

        return expr.MethodCallExpression(
            [(Duration, int, api.Expression.duration_hours)],
            "dt.hours",
            self._expression,
        )

    def days(self) -> expr.ColumnExpression:
        """The total number of days in a Duration.

        Returns:
            Days as int.

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |         t1          |         t2
        ...    0 | 2023-03-15T00:00:00 | 2023-05-15T10:13:23
        ...    1 | 2023-04-15T00:00:00 | 2023-05-15T10:00:00
        ...    2 | 2023-05-01T10:00:00 | 2023-05-15T10:00:00
        ...    3 | 2023-05-15T10:00:00 | 2023-05-15T09:00:00
        ...    4 | 2023-05-15T10:00:00 | 2023-05-15T11:00:00
        ...    5 | 2023-05-16T12:13:00 | 2023-05-15T10:00:00
        ...    6 | 2024-05-15T14:13:23 | 2023-05-15T10:00:00
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S"
        >>> table_with_datetimes = table.select(
        ...     t1=pw.this.t1.dt.strptime(fmt=fmt), t2=pw.this.t2.dt.strptime(fmt=fmt)
        ... )
        >>> table_with_diff = table_with_datetimes.select(diff=pw.this.t1 - pw.this.t2)
        >>> table_with_days = table_with_diff.select(days=pw.this["diff"].dt.days())
        >>> pw.debug.compute_and_print(table_with_days, include_id=False)
        days
        -61
        -30
        -14
        0
        0
        1
        366
        """

        return expr.MethodCallExpression(
            [(Duration, int, api.Expression.duration_days)],
            "dt.days",
            self._expression,
        )

    def weeks(self) -> expr.ColumnExpression:
        """The total number of weeks in a Duration.

        Returns:
            Weeks as int.

        Example:

        >>> import pathway as pw
        >>> table = pw.debug.table_from_markdown(
        ...     '''
        ...      |         t1          |         t2
        ...    0 | 2023-03-15T00:00:00 | 2023-05-15T10:13:23
        ...    1 | 2023-04-15T00:00:00 | 2023-05-15T10:00:00
        ...    2 | 2023-05-01T10:00:00 | 2023-05-15T10:00:00
        ...    3 | 2023-05-15T10:00:00 | 2023-05-15T09:00:00
        ...    4 | 2023-05-15T10:00:00 | 2023-05-15T11:00:00
        ...    5 | 2023-05-16T12:13:00 | 2023-05-15T10:00:00
        ...    6 | 2024-05-15T14:13:23 | 2023-05-15T10:00:00
        ... '''
        ... )
        >>> fmt = "%Y-%m-%dT%H:%M:%S"
        >>> table_with_datetimes = table.select(
        ...     t1=pw.this.t1.dt.strptime(fmt=fmt), t2=pw.this.t2.dt.strptime(fmt=fmt)
        ... )
        >>> table_with_diff = table_with_datetimes.select(diff=pw.this.t1 - pw.this.t2)
        >>> table_with_weeks = table_with_diff.select(weeks=pw.this["diff"].dt.weeks())
        >>> pw.debug.compute_and_print(table_with_weeks, include_id=False)
        weeks
        -8
        -4
        -2
        0
        0
        0
        52
        """
        return expr.MethodCallExpression(
            [(Duration, int, api.Expression.duration_weeks)],
            "dt.weeks",
            self._expression,
        )

    def from_timestamp(self, unit: str) -> expr.ColumnExpression:
        """
        Converts timestamp represented as an int to DateTime.

        Args:
            timestamp: value to be converted to DateTime
            unit: unit of a timestamp. It has to be one of 's', 'ms', 'us', 'ns'

        Returns:
            DateTime

        Example:

        >>> import pathway as pw
        >>> fmt = "%Y-%m-%dT%H:%M:%S"
        >>> t1 = pw.debug.table_from_markdown(
        ...     '''
        ...   | timestamp
        ... 1 |    10
        ... 2 | 1685969950
        ... '''
        ... )
        >>> t2 = t1.select(date=pw.this.timestamp.dt.from_timestamp(unit="s"))
        >>> pw.debug.compute_and_print(t2, include_id=False)
        date
        1970-01-01 00:00:10
        2023-06-05 12:59:10
        """
        if unit not in ("s", "ms", "us", "ns"):
            raise ValueError(f"unit has to be one of s, ms, us, ns but is {unit}.")
        return expr.MethodCallExpression(
            [
                (
                    (int, str),
                    DateTimeNaive,
                    api.Expression.date_time_naive_from_timestamp,
                ),
            ],
            "datetime_from_timestamp",
            self._expression,
            unit,
        )
