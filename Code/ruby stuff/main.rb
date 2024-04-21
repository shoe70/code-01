# Hello, World

def scroll_text(text, scroll_speed)
  text.each_char do |char|
    print char
    $stdout.flush
    sleep scroll_speed
  end
end

scroll_speed = 0.03
scroll_text("Hello, World!", scroll_speed)