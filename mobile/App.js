
import { useMemo, useRef, useState } from "react";
import {
  KeyboardAvoidingView,
  Platform,
  Pressable,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  View,
  useWindowDimensions,
} from "react-native";

import { QUICK_AREAS, SUGGESTIONS, respond } from "./src/assistant";

const INITIAL_MESSAGES = [
  {
    id: "intro",
    role: "assistant",
    area: "Inicio",
    title: "Lista para ayudarte",
    text: "Hola, Areli. Soy tu asistente para codigo, tareas, seguridad, SQL, Git y calma mental cuando el bug se pone intenso. Escribeme como hablas normalmente y yo lo ordeno contigo.",
  },
];

function createId() {
  return `${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

function MessageBubble({ message }) {
  const isUser = message.role === "user";

  return (
    <View style={[styles.messageRow, isUser && styles.messageRowUser]}>
      <View style={[styles.bubble, isUser ? styles.userBubble : styles.assistantBubble]}>
        {!isUser && (
          <View style={styles.messageMeta}>
            <Text style={styles.areaText}>{message.area}</Text>
            <Text style={styles.titleText}>{message.title}</Text>
          </View>
        )}
        <Text style={[styles.messageText, isUser && styles.userMessageText]}>{message.text}</Text>
      </View>
    </View>
  );
}

function QuickChip({ label, onPress }) {
  return (
    <Pressable style={({ pressed }) => [styles.quickChip, pressed && styles.pressed]} onPress={onPress}>
      <Text style={styles.quickChipText}>{label}</Text>
    </Pressable>
  );
}

function InsightPanel({ count, onSuggestion }) {
  return (
    <View style={styles.insightPanel}>
      <Text style={styles.insightEyebrow}>Centro de mando</Text>
      <Text style={styles.insightTitle}>Preguntame sin pena, aunque vaya con dedazos.</Text>
      <Text style={styles.insightCopy}>
        Yo intento detectar intencion, tema y siguiente paso. Si falta contexto, te lo pido sin hacerte perder tiempo.
      </Text>

      <View style={styles.metricRow}>
        <View style={styles.metricBox}>
          <Text style={styles.metricValue}>{count}</Text>
          <Text style={styles.metricLabel}>mensajes</Text>
        </View>
        <View style={styles.metricBoxAlt}>
          <Text style={styles.metricValueAlt}>3</Text>
          <Text style={styles.metricLabelAlt}>pasos claros</Text>
        </View>
      </View>

      <Text style={styles.insightSectionTitle}>Prueba esto</Text>
      {SUGGESTIONS.slice(0, 3).map((suggestion) => (
        <Pressable
          key={suggestion}
          style={({ pressed }) => [styles.sideSuggestion, pressed && styles.pressed]}
          onPress={() => onSuggestion(suggestion)}
        >
          <Text style={styles.sideSuggestionText}>{suggestion}</Text>
        </Pressable>
      ))}
    </View>
  );
}

export default function App() {
  const [messages, setMessages] = useState(INITIAL_MESSAGES);
  const [input, setInput] = useState("");
  const scrollRef = useRef(null);
  const { width } = useWindowDimensions();
  const isWide = width >= 900;

  const userMessagesCount = useMemo(
    () => messages.filter((message) => message.role === "user").length,
    [messages],
  );

  const sendMessage = (value = input) => {
    const text = value.trim();

    if (!text) {
      return;
    }

    const userMessage = {
      id: createId(),
      role: "user",
      text,
    };

    const assistantResponse = respond(text, [...messages, userMessage]);
    const assistantMessage = {
      id: createId(),
      role: "assistant",
      ...assistantResponse,
    };

    setMessages((current) => [...current, userMessage, assistantMessage]);
    setInput("");
    setTimeout(() => scrollRef.current?.scrollToEnd({ animated: true }), 50);
  };

  const clearChat = () => {
    setMessages(INITIAL_MESSAGES);
    setInput("");
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#F6F8FB" />
      <KeyboardAvoidingView
        style={styles.screen}
        behavior={Platform.OS === "ios" ? "padding" : undefined}
      >
        <View style={styles.header}>
          <View>
            <Text style={styles.eyebrow}>VitraMind AI</Text>
            <Text style={styles.heading}>Areli, vamos paso a paso</Text>
          </View>
          <Pressable style={({ pressed }) => [styles.iconButton, pressed && styles.pressed]} onPress={clearChat}>
            <Text style={styles.iconButtonText}>CL</Text>
          </Pressable>
        </View>

        <View style={[styles.workspace, isWide && styles.workspaceWide]}>
          {isWide && <InsightPanel count={userMessagesCount} onSuggestion={sendMessage} />}

          <View style={styles.chatShell}>
            <View style={styles.statusBand}>
              <View>
                <Text style={styles.statusLabel}>Modo</Text>
                <Text style={styles.statusValue}>Humano y tecnico</Text>
              </View>
              <View style={styles.statusDivider} />
              <View>
                <Text style={styles.statusLabel}>Contexto</Text>
                <Text style={styles.statusValue}>{userMessagesCount} mensajes</Text>
              </View>
            </View>

            <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.quickArea}>
              {QUICK_AREAS.map((area) => (
                <QuickChip key={area} label={area} onPress={() => sendMessage(`Ayudame con ${area}`)} />
              ))}
            </ScrollView>

            <ScrollView
              ref={scrollRef}
              style={styles.chat}
              contentContainerStyle={styles.chatContent}
              showsVerticalScrollIndicator={false}
            >
              {messages.map((message) => (
                <MessageBubble key={message.id} message={message} />
              ))}

              {messages.length === 1 && !isWide && (
                <View style={styles.suggestionPanel}>
                  <Text style={styles.suggestionTitle}>Ideas para empezar</Text>
                  {SUGGESTIONS.map((suggestion) => (
                    <Pressable
                      key={suggestion}
                      style={({ pressed }) => [styles.suggestionButton, pressed && styles.pressed]}
                      onPress={() => sendMessage(suggestion)}
                    >
                      <Text style={styles.suggestionText}>{suggestion}</Text>
                    </Pressable>
                  ))}
                </View>
              )}
            </ScrollView>

            <View style={styles.composer}>
              <TextInput
                style={styles.input}
                value={input}
                onChangeText={setInput}
                placeholder="Escribe tu duda, error o idea..."
                placeholderTextColor="#6F7480"
                multiline
              />
              <Pressable style={({ pressed }) => [styles.sendButton, pressed && styles.pressed]} onPress={() => sendMessage()}>
                <Text style={styles.sendButtonText}>Enviar</Text>
              </Pressable>
            </View>
          </View>
        </View>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: "#F6F8FB",
  },
  screen: {
    flex: 1,
    paddingHorizontal: 18,
    paddingTop: 12,
  },
  header: {
    alignItems: "center",
    flexDirection: "row",
    justifyContent: "space-between",
    paddingBottom: 14,
  },
  eyebrow: {
    color: "#0F766E",
    fontSize: 12,
    fontWeight: "800",
    letterSpacing: 0,
    textTransform: "uppercase",
  },
  heading: {
    color: "#141821",
    fontSize: 24,
    fontWeight: "800",
    letterSpacing: 0,
    marginTop: 3,
  },
  iconButton: {
    alignItems: "center",
    backgroundColor: "#141821",
    borderRadius: 8,
    height: 42,
    justifyContent: "center",
    width: 42,
  },
  iconButtonText: {
    color: "#FFFFFF",
    fontSize: 12,
    fontWeight: "900",
    letterSpacing: 0,
  },
  statusBand: {
    alignItems: "center",
    backgroundColor: "#FFFFFF",
    borderColor: "#DCE3EA",
    borderRadius: 8,
    borderWidth: 1,
    flexDirection: "row",
    justifyContent: "space-between",
    paddingHorizontal: 16,
    paddingVertical: 12,
  },
  statusLabel: {
    color: "#6F7480",
    fontSize: 12,
    fontWeight: "700",
    letterSpacing: 0,
  },
  statusValue: {
    color: "#141821",
    fontSize: 14,
    fontWeight: "800",
    letterSpacing: 0,
    marginTop: 2,
  },
  statusDivider: {
    backgroundColor: "#DCE3EA",
    height: 32,
    width: 1,
  },
  quickArea: {
    flexGrow: 0,
    marginTop: 12,
    maxHeight: 40,
  },
  quickChip: {
    alignItems: "center",
    backgroundColor: "#E8F5F3",
    borderColor: "#A9D9D2",
    borderRadius: 8,
    borderWidth: 1,
    height: 36,
    justifyContent: "center",
    marginRight: 8,
    paddingHorizontal: 14,
  },
  quickChipText: {
    color: "#0F766E",
    fontSize: 13,
    fontWeight: "800",
    letterSpacing: 0,
  },
  chat: {
    flex: 1,
    marginTop: 14,
  },
  chatContent: {
    paddingBottom: 18,
  },
  messageRow: {
    alignItems: "flex-start",
    marginBottom: 12,
  },
  messageRowUser: {
    alignItems: "flex-end",
  },
  bubble: {
    borderRadius: 8,
    maxWidth: "88%",
    paddingHorizontal: 14,
    paddingVertical: 12,
  },
  assistantBubble: {
    backgroundColor: "#FFFFFF",
    borderColor: "#DCE3EA",
    borderWidth: 1,
  },
  userBubble: {
    backgroundColor: "#2447A3",
  },
  messageMeta: {
    borderBottomColor: "#E8EDF3",
    borderBottomWidth: 1,
    marginBottom: 8,
    paddingBottom: 7,
  },
  areaText: {
    color: "#D65A31",
    fontSize: 11,
    fontWeight: "900",
    letterSpacing: 0,
    textTransform: "uppercase",
  },
  titleText: {
    color: "#141821",
    fontSize: 15,
    fontWeight: "900",
    letterSpacing: 0,
    marginTop: 2,
  },
  messageText: {
    color: "#2D3440",
    fontSize: 15,
    letterSpacing: 0,
    lineHeight: 22,
  },
  userMessageText: {
    color: "#FFFFFF",
    fontWeight: "700",
  },
  suggestionPanel: {
    borderColor: "#DCE3EA",
    borderRadius: 8,
    borderWidth: 1,
    marginTop: 8,
    padding: 12,
  },
  suggestionTitle: {
    color: "#141821",
    fontSize: 14,
    fontWeight: "900",
    letterSpacing: 0,
    marginBottom: 8,
  },
  suggestionButton: {
    backgroundColor: "#FFFFFF",
    borderColor: "#DCE3EA",
    borderRadius: 8,
    borderWidth: 1,
    marginTop: 8,
    paddingHorizontal: 12,
    paddingVertical: 10,
  },
  suggestionText: {
    color: "#2D3440",
    fontSize: 14,
    fontWeight: "700",
    letterSpacing: 0,
  },
  composer: {
    alignItems: "flex-end",
    backgroundColor: "#F6F8FB",
    borderTopColor: "#DCE3EA",
    borderTopWidth: 1,
    flexDirection: "row",
    gap: 10,
    paddingBottom: 12,
    paddingTop: 12,
  },
  input: {
    backgroundColor: "#FFFFFF",
    borderColor: "#C9D3DF",
    borderRadius: 8,
    borderWidth: 1,
    color: "#141821",
    flex: 1,
    fontSize: 15,
    letterSpacing: 0,
    maxHeight: 112,
    minHeight: 46,
    paddingHorizontal: 12,
    paddingVertical: 11,
  },
  sendButton: {
    alignItems: "center",
    backgroundColor: "#D65A31",
    borderRadius: 8,
    height: 46,
    justifyContent: "center",
    paddingHorizontal: 16,
  },
  sendButtonText: {
    color: "#FFFFFF",
    fontSize: 14,
    fontWeight: "900",
    letterSpacing: 0,
  },
  pressed: {
    opacity: 0.72,
  },
  workspace: {
    flex: 1,
  },
  workspaceWide: {
    alignSelf: "center",
    flexDirection: "row",
    gap: 16,
    maxWidth: 1160,
    width: "100%",
  },
  chatShell: {
    flex: 1,
  },
  insightPanel: {
    backgroundColor: "#141821",
    borderRadius: 8,
    marginTop: 0,
    padding: 18,
    width: 320,
  },
  insightEyebrow: {
    color: "#66D3C7",
    fontSize: 12,
    fontWeight: "900",
    letterSpacing: 0,
    textTransform: "uppercase",
  },
  insightTitle: {
    color: "#FFFFFF",
    fontSize: 23,
    fontWeight: "900",
    letterSpacing: 0,
    lineHeight: 29,
    marginTop: 8,
  },
  insightCopy: {
    color: "#C6D1DF",
    fontSize: 14,
    letterSpacing: 0,
    lineHeight: 21,
    marginTop: 10,
  },
  metricRow: {
    flexDirection: "row",
    gap: 10,
    marginTop: 18,
  },
  metricBox: {
    backgroundColor: "#2447A3",
    borderRadius: 8,
    flex: 1,
    padding: 12,
  },
  metricBoxAlt: {
    backgroundColor: "#0F766E",
    borderRadius: 8,
    flex: 1,
    padding: 12,
  },
  metricValue: {
    color: "#FFFFFF",
    fontSize: 24,
    fontWeight: "900",
    letterSpacing: 0,
  },
  metricValueAlt: {
    color: "#FFFFFF",
    fontSize: 24,
    fontWeight: "900",
    letterSpacing: 0,
  },
  metricLabel: {
    color: "#D9E2F2",
    fontSize: 12,
    fontWeight: "700",
    letterSpacing: 0,
    marginTop: 2,
  },
  metricLabelAlt: {
    color: "#D9F2EE",
    fontSize: 12,
    fontWeight: "700",
    letterSpacing: 0,
    marginTop: 2,
  },
  insightSectionTitle: {
    color: "#FFFFFF",
    fontSize: 14,
    fontWeight: "900",
    letterSpacing: 0,
    marginTop: 22,
  },
  sideSuggestion: {
    backgroundColor: "#242B38",
    borderColor: "#354154",
    borderRadius: 8,
    borderWidth: 1,
    marginTop: 9,
    paddingHorizontal: 12,
    paddingVertical: 11,
  },
  sideSuggestionText: {
    color: "#EEF3F8",
    fontSize: 13,
    fontWeight: "800",
    letterSpacing: 0,
    lineHeight: 18,
  },
});
