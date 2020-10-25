/**
* This file is part of ORB-SLAM2.
*
* Copyright (C) 2014-2016 Raúl Mur-Artal <raulmur at unizar dot es> (University
*of Zaragoza) && Shaifali Parashar, Adrien Bartoli (Université Clermont Auvergne)
* For more information see <https://github.com/raulmur/ORB_SLAM2>
*
* ORB-SLAM2 is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* ORB-SLAM2 is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with ORB-SLAM2. If not, see <http://www.gnu.org/licenses/>.
*/

#ifndef MAPPOINT_H
#define MAPPOINT_H

#include "Frame.h"
#include "KeyFrame.h"
#include "Map.h"

#include <map>
#include <mutex>
#include <opencv2/core/core.hpp>
namespace ORB_SLAM2
{

  class KeyFrame;
  class Map;
  class Frame;

  class MapPoint
  {
  public:
    MapPoint() = default;
    MapPoint(const int number);
    virtual ~MapPoint() = default;
    
  public:
    static long unsigned int nNextId;
    // static std::mutex mGlobalMutex;
  };

} // namespace ORB_SLAM2

#endif // MAPPOINT_H
