#ifndef POLYGON_BASE_REGULAR_POLYGON_CPP
#define POLYGON_BASE_REGULAR_POLYGON_CPP

namespace polygon_base
{
    class RegularPolygon
    {
    public:
        virtual void initialize(double side_length) = 0;
        virtual double area() = 0;
        virtual ~RegularPolygon() {}

    protected:
        RegularPolygon() {} // pluginlib requires a constructor with no arguments
    };
} // namespace polygon_base

#endif // POLYGON_BASE_REGULAR_POLYGON_CPP