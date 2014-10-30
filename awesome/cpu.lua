jiffies = {}
  function activecpu()
    local s = "cpu:"
    local i = 0
    for line in io.lines("/proc/stat") do
      if i == 1 then 
      local cpu, newjiffies = string.match(line, "(cpu%d*)\ +(%d+)")
      if cpu and newjiffies then
        if not jiffies[cpu] then
          jiffies[cpu] = newjiffies                                                                              
        end
        --The string.format prevents your task list from jumping around 
        --when CPU usage goes above/below 10%
        s = s .. string.format("%.03d", newjiffies-jiffies[cpu]) .. "% - "
        jiffies[cpu] = newjiffies
      end
      else
        i =1
      end
    end
    return s
  end

cpuinfo = widget({ type = "textbox", align = "right" })

awful.hooks.timer.register(3, function() cpuinfo.text = activecpu() end)

