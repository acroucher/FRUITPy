module setup_module

  implicit none

  real, public :: x = 0.0

  contains

!------------------------------------------------------------------------

    subroutine setup

      x = 3.14

    end subroutine setup

!------------------------------------------------------------------------

    subroutine teardown

      x = 0.0

    end subroutine teardown

!------------------------------------------------------------------------

end module setup_module
