! This comment contains the word 'module'

module adder_module

  ! Module for adding numbers.

  implicit none
  private

  type adder_type
     private
     real, public :: a, b, result
   contains
     private
     procedure, public :: init => adder_init
     procedure, public :: add => adder_add
  end type adder_type

public :: adder_type

!------------------------------------------------------------------------

contains

!------------------------------------------------------------------------

  subroutine adder_init(self, a, b)
    class(adder_type), intent(in out) :: self
    real, intent(in) :: a, b

    self%a = a
    self%b = b

  end subroutine adder_init

!------------------------------------------------------------------------

  subroutine adder_add(self)
    class(adder_type), intent(in out) :: self

    self%result = self%a + self%b

  end subroutine adder_init

!------------------------------------------------------------------------

end module adder_module
