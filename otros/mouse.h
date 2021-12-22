#ifndef MOUSE_OBJ_H
#define MOUSE_OBJ_H
 
#include "UIObject.h"
#include "Command.h"
#include "NameList.h"
 
class Mouse : public UIObject {
public:
  enum MoveMode {ROTATION, TRANSLATION, SCALING, LIGHT, USERPOINT, 
  PICK, QUERY, CENTER, \
  LABELATOM, LABELBOND, LABELANGLE, LABELDIHEDRAL, \
  MOVEATOM, MOVERES, MOVEFRAG, MOVEMOL, MOVEREP,\
  FORCEATOM, FORCERES, FORCEFRAG, \
  ADDBOND};

  enum MouseButton { B_NONE = 0, B_LEFT = 1, B_MIDDLE, B_RIGHT };
 
  static const char *get_mode_str(MoveMode mode);
 
  private:
  MoveMode moveMode;          
  MouseButton pickInProgress; 
  int moveObj;                
  int currX, currY;           
  int oldX, oldY;             
  MouseButton buttonDown;     

float transInc, rotInc, scaleInc;
float xRotVel, yRotVel, zRotVel, scaling, RotVelScale;
int rocking_enabled;
int mouse_moved(void);
int mouse_userpoint(void);
void handle_winevent(long, long); 
public:
Mouse(VMDApp *);
virtual ~Mouse(void);
virtual void reset(void);
int move_mode(MoveMode, int = 0);
void stop_rotation(void);
virtual int check_event(void);
void set_rocking(int on);
};
class CmdMouseMode : public Command {
public:
CmdMouseMode(int mm, int ms)
: Command(MOUSE_MODE), mouseMode(mm), mouseSetting(ms) {}
int mouseMode, mouseSetting;
};
#endif
 
