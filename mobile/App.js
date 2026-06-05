
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

import { FEATURE_IDEAS, QUICK_AREAS, SUGGESTIONS, USER_MODES, respond } from "./src/assistant";

const INITIAL_MESSAGES = [
  {
    id: "intro",
    role: "assistant",
    area: "Inicio",
    title: "Asistente listo",
    text: "Hola, Areli. Tengo listo el espacio para ordenar codigo, tareas, SQL, Git, seguridad e ideas de producto. Escribe como te salga; yo convierto la idea en pasos claros.",
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
        {!isUser && message.insights?.length > 0 && (
          <View style={styles.insightChips}>
            {message.insights.map((item) => (
              <View key={item} style={styles.insightChip}>
                <Text style={styles.insightChipText}>{item}</Text>
              </View>
            ))}
          </View>
        )}
        {!isUser && message.actions?.length > 0 && (
          <View style={styles.actionList}>
            {message.actions.map((action) => (
              <View key={action} style={styles.actionPill}>
                <Text style={styles.actionPillText}>{action}</Text>
              </View>
            ))}
          </View>
        )}
      </View>
    </View>
  );
}

function IconText({ icon, label }) {
  return (
    <View style={styles.iconText}>
      <Text style={styles.iconTextIcon}>{icon}</Text>
      <Text style={styles.iconTextLabel}>{label}</Text>
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

function ModeChip({ mode, active, onPress }) {
  return (
    <Pressable style={({ pressed }) => [styles.modeChip, active && styles.modeChipActive, pressed && styles.pressed]} onPress={onPress}>
      <Text style={[styles.modeChipText, active && styles.modeChipTextActive]}>{mode.label}</Text>
    </Pressable>
  );
}

function InsightPanel({ count, selectedMode, onModeChange, onSuggestion }) {
  const currentMode = USER_MODES.find((mode) => mode.id === selectedMode) || USER_MODES[0];

  return (
    <View style={styles.insightPanel}>
      <Text style={styles.insightEyebrow}>Workspace</Text>
      <Text style={styles.insightTitle}>VitraMind AI</Text>
      <Text style={styles.insightCopy}>Asistente personal para desarrollo, organizacion y decisiones tecnicas.</Text>

      <View style={styles.metricRow}>
        <View style={styles.metricBox}>
          <Text style={styles.metricValue}>{count}</Text>
          <Text style={styles.metricLabel}>mensajes</Text>
        </View>
        <View style={styles.metricBoxAlt}>
          <Text style={styles.metricValueAlt}>{USER_MODES.length}</Text>
          <Text style={styles.metricLabelAlt}>modos</Text>
        </View>
      </View>

      <View style={styles.focusBox}>
        <IconText icon="01" label="Detecta tema, energia y formato." />
        <IconText icon="02" label="Propone acciones despues de responder." />
        <IconText icon="03" label="Mantiene contexto reciente del chat." />
      </View>

      <Text style={styles.insightSectionTitle}>Modo de respuesta</Text>
      <View style={styles.modeWrap}>
        {USER_MODES.map((mode) => (
          <ModeChip
            key={mode.id}
            mode={mode}
            active={mode.id === selectedMode}
            onPress={() => onModeChange(mode.id)}
          />
        ))}
      </View>
      <Text style={styles.modeDescription}>{currentMode.description}</Text>

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

      <Text style={styles.insightSectionTitle}>Podemos agregar</Text>
      {FEATURE_IDEAS.slice(0, 3).map((idea) => (
        <View key={idea} style={styles.ideaItem}>
          <Text style={styles.ideaText}>{idea}</Text>
        </View>
      ))}
    </View>
  );
}

export default function App() {
  const [messages, setMessages] = useState(INITIAL_MESSAGES);
  const [input, setInput] = useState("");
  const [selectedMode, setSelectedMode] = useState("normal");
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

    const assistantResponse = respond(text, [...messages, userMessage], selectedMode);
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
            <Text style={styles.heading}>Panel de trabajo</Text>
          </View>
          <Pressable style={({ pressed }) => [styles.iconButton, pressed && styles.pressed]} onPress={clearChat}>
            <Text style={styles.iconButtonText}>Limpiar</Text>
          </Pressable>
        </View>

        <View style={[styles.workspace, isWide && styles.workspaceWide]}>
          {isWide && (
            <InsightPanel
              count={userMessagesCount}
              selectedMode={selectedMode}
              onModeChange={setSelectedMode}
              onSuggestion={sendMessage}
            />
          )}

          <View style={styles.chatShell}>
            <View style={styles.projectStrip}>
              <View>
                <Text style={styles.projectLabel}>Proyecto activo</Text>
                <Text style={styles.projectTitle}>IA_Areli / Asistente personal</Text>
              </View>
              <View style={styles.projectBadge}>
                <Text style={styles.projectBadgeText}>Local</Text>
              </View>
            </View>

            <View style={styles.statusBand}>
              <View>
                <Text style={styles.statusLabel}>Modo</Text>
                <Text style={styles.statusValue}>Tecnico</Text>
              </View>
              <View style={styles.statusDivider} />
              <View>
                <Text style={styles.statusLabel}>Contexto</Text>
                <Text style={styles.statusValue}>{userMessagesCount} mensajes</Text>
              </View>
              <View style={styles.statusDivider} />
              <View>
                <Text style={styles.statusLabel}>Tono</Text>
                <Text style={styles.statusValue}>{USER_MODES.find((mode) => mode.id === selectedMode)?.label}</Text>
              </View>
            </View>

            {!isWide && (
              <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.modeArea}>
                {USER_MODES.map((mode) => (
                  <ModeChip
                    key={mode.id}
                    mode={mode}
                    active={mode.id === selectedMode}
                    onPress={() => setSelectedMode(mode.id)}
                  />
                ))}
              </ScrollView>
            )}

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

                  <Text style={styles.suggestionTitleAlt}>Que podemos agregar</Text>
                  {FEATURE_IDEAS.slice(0, 4).map((idea) => (
                    <View key={idea} style={styles.mobileIdeaItem}>
                      <Text style={styles.mobileIdeaText}>{idea}</Text>
                    </View>
                  ))}
                </View>
              )}
            </ScrollView>

            <View style={styles.composer}>
              <TextInput
                style={styles.input}
                value={input}
                onChangeText={setInput}
                placeholder="Escribe una duda, error, tarea o idea..."
                placeholderTextColor="#6F7480"
                multiline
              />
              <Pressable
                style={({ pressed }) => [
                  styles.sendButton,
                  !input.trim() && styles.sendButtonDisabled,
                  pressed && styles.pressed,
                ]}
                onPress={() => sendMessage()}
              >
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
    backgroundColor: "#F4F6F8",
  },
  screen: {
    flex: 1,
    paddingHorizontal: 20,
    paddingTop: 14,
  },
  header: {
    alignItems: "center",
    flexDirection: "row",
    justifyContent: "space-between",
    paddingBottom: 16,
  },
  eyebrow: {
    color: "#36527A",
    fontSize: 12,
    fontWeight: "800",
    letterSpacing: 0,
    textTransform: "uppercase",
  },
  heading: {
    color: "#111827",
    fontSize: 26,
    fontWeight: "800",
    letterSpacing: 0,
    marginTop: 3,
  },
  iconButton: {
    alignItems: "center",
    backgroundColor: "#111827",
    borderRadius: 8,
    height: 40,
    justifyContent: "center",
    paddingHorizontal: 14,
  },
  iconButtonText: {
    color: "#FFFFFF",
    fontSize: 13,
    fontWeight: "900",
    letterSpacing: 0,
  },
  projectStrip: {
    alignItems: "center",
    backgroundColor: "#FFFFFF",
    borderColor: "#D8DEE8",
    borderRadius: 8,
    borderWidth: 1,
    flexDirection: "row",
    justifyContent: "space-between",
    marginBottom: 12,
    paddingHorizontal: 16,
    paddingVertical: 13,
  },
  projectLabel: {
    color: "#697386",
    fontSize: 11,
    fontWeight: "800",
    letterSpacing: 0,
    textTransform: "uppercase",
  },
  projectTitle: {
    color: "#111827",
    fontSize: 15,
    fontWeight: "900",
    letterSpacing: 0,
    marginTop: 2,
  },
  projectBadge: {
    backgroundColor: "#EEF7F5",
    borderColor: "#B8DCD6",
    borderRadius: 8,
    borderWidth: 1,
    paddingHorizontal: 10,
    paddingVertical: 6,
  },
  projectBadgeText: {
    color: "#0B6B61",
    fontSize: 12,
    fontWeight: "900",
    letterSpacing: 0,
  },
  statusBand: {
    alignItems: "center",
    backgroundColor: "#FFFFFF",
    borderColor: "#D8DEE8",
    borderRadius: 8,
    borderWidth: 1,
    flexDirection: "row",
    justifyContent: "space-between",
    paddingHorizontal: 16,
    paddingVertical: 12,
  },
  statusLabel: {
    color: "#697386",
    fontSize: 12,
    fontWeight: "700",
    letterSpacing: 0,
  },
  statusValue: {
    color: "#111827",
    fontSize: 14,
    fontWeight: "800",
    letterSpacing: 0,
    marginTop: 2,
  },
  statusDivider: {
    backgroundColor: "#D8DEE8",
    height: 32,
    width: 1,
  },
  quickArea: {
    flexGrow: 0,
    marginTop: 12,
    maxHeight: 40,
  },
  modeArea: {
    flexGrow: 0,
    marginTop: 10,
    maxHeight: 38,
  },
  quickChip: {
    alignItems: "center",
    backgroundColor: "#FFFFFF",
    borderColor: "#CBD5E1",
    borderRadius: 8,
    borderWidth: 1,
    height: 36,
    justifyContent: "center",
    marginRight: 8,
    paddingHorizontal: 14,
  },
  quickChipText: {
    color: "#334155",
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
    maxWidth: "90%",
    paddingHorizontal: 15,
    paddingVertical: 13,
  },
  assistantBubble: {
    backgroundColor: "#FFFFFF",
    borderColor: "#D8DEE8",
    borderWidth: 1,
  },
  userBubble: {
    backgroundColor: "#1F3A68",
  },
  messageMeta: {
    borderBottomColor: "#E9EEF5",
    borderBottomWidth: 1,
    marginBottom: 8,
    paddingBottom: 7,
  },
  areaText: {
    color: "#B45309",
    fontSize: 11,
    fontWeight: "900",
    letterSpacing: 0,
    textTransform: "uppercase",
  },
  titleText: {
    color: "#111827",
    fontSize: 15,
    fontWeight: "900",
    letterSpacing: 0,
    marginTop: 2,
  },
  messageText: {
    color: "#273142",
    fontSize: 15,
    letterSpacing: 0,
    lineHeight: 22,
  },
  userMessageText: {
    color: "#FFFFFF",
    fontWeight: "700",
  },
  insightChips: {
    flexDirection: "row",
    flexWrap: "wrap",
    gap: 6,
    marginTop: 12,
  },
  insightChip: {
    backgroundColor: "#F0F7F5",
    borderColor: "#C7E2DD",
    borderRadius: 8,
    borderWidth: 1,
    paddingHorizontal: 8,
    paddingVertical: 5,
  },
  insightChipText: {
    color: "#0B6B61",
    fontSize: 11,
    fontWeight: "800",
    letterSpacing: 0,
  },
  actionList: {
    flexDirection: "row",
    flexWrap: "wrap",
    gap: 7,
    marginTop: 9,
  },
  actionPill: {
    backgroundColor: "#FFF7ED",
    borderColor: "#FED7AA",
    borderRadius: 8,
    borderWidth: 1,
    paddingHorizontal: 9,
    paddingVertical: 6,
  },
  actionPillText: {
    color: "#9A3412",
    fontSize: 12,
    fontWeight: "900",
    letterSpacing: 0,
  },
  suggestionPanel: {
    backgroundColor: "#FFFFFF",
    borderColor: "#D8DEE8",
    borderRadius: 8,
    borderWidth: 1,
    marginTop: 8,
    padding: 12,
  },
  suggestionTitle: {
    color: "#111827",
    fontSize: 14,
    fontWeight: "900",
    letterSpacing: 0,
    marginBottom: 8,
  },
  suggestionButton: {
    backgroundColor: "#F8FAFC",
    borderColor: "#E2E8F0",
    borderRadius: 8,
    borderWidth: 1,
    marginTop: 8,
    paddingHorizontal: 12,
    paddingVertical: 10,
  },
  suggestionText: {
    color: "#273142",
    fontSize: 14,
    fontWeight: "700",
    letterSpacing: 0,
  },
  composer: {
    alignItems: "flex-end",
    backgroundColor: "#F4F6F8",
    borderTopColor: "#D8DEE8",
    borderTopWidth: 1,
    flexDirection: "row",
    gap: 10,
    paddingBottom: 12,
    paddingTop: 12,
  },
  input: {
    backgroundColor: "#FFFFFF",
    borderColor: "#C3CCD9",
    borderRadius: 8,
    borderWidth: 1,
    color: "#111827",
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
    backgroundColor: "#B45309",
    borderRadius: 8,
    height: 46,
    justifyContent: "center",
    paddingHorizontal: 16,
  },
  sendButtonDisabled: {
    backgroundColor: "#9CA3AF",
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
    gap: 18,
    maxWidth: 1200,
    width: "100%",
  },
  chatShell: {
    flex: 1,
  },
  insightPanel: {
    backgroundColor: "#111827",
    borderRadius: 8,
    marginTop: 0,
    padding: 18,
    width: 328,
  },
  insightEyebrow: {
    color: "#93C5FD",
    fontSize: 12,
    fontWeight: "900",
    letterSpacing: 0,
    textTransform: "uppercase",
  },
  insightTitle: {
    color: "#FFFFFF",
    fontSize: 25,
    fontWeight: "900",
    letterSpacing: 0,
    lineHeight: 29,
    marginTop: 8,
  },
  insightCopy: {
    color: "#CBD5E1",
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
    backgroundColor: "#1F3A68",
    borderRadius: 8,
    flex: 1,
    padding: 12,
  },
  metricBoxAlt: {
    backgroundColor: "#0B6B61",
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
  focusBox: {
    backgroundColor: "#172033",
    borderColor: "#27354F",
    borderRadius: 8,
    borderWidth: 1,
    gap: 10,
    marginTop: 16,
    padding: 12,
  },
  iconText: {
    alignItems: "flex-start",
    flexDirection: "row",
    gap: 9,
  },
  iconTextIcon: {
    color: "#93C5FD",
    fontSize: 12,
    fontWeight: "900",
    letterSpacing: 0,
    width: 22,
  },
  iconTextLabel: {
    color: "#D8E1EE",
    flex: 1,
    fontSize: 12,
    fontWeight: "700",
    letterSpacing: 0,
    lineHeight: 17,
  },
  insightSectionTitle: {
    color: "#FFFFFF",
    fontSize: 14,
    fontWeight: "900",
    letterSpacing: 0,
    marginTop: 22,
  },
  sideSuggestion: {
    backgroundColor: "#172033",
    borderColor: "#27354F",
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
  modeWrap: {
    flexDirection: "row",
    flexWrap: "wrap",
    gap: 8,
    marginTop: 10,
  },
  modeChip: {
    backgroundColor: "#172033",
    borderColor: "#27354F",
    borderRadius: 8,
    borderWidth: 1,
    height: 32,
    justifyContent: "center",
    paddingHorizontal: 10,
  },
  modeChipActive: {
    backgroundColor: "#93C5FD",
    borderColor: "#93C5FD",
  },
  modeChipText: {
    color: "#DDE6F0",
    fontSize: 12,
    fontWeight: "900",
    letterSpacing: 0,
  },
  modeChipTextActive: {
    color: "#0F172A",
  },
  modeDescription: {
    color: "#B8C5D4",
    fontSize: 12,
    fontWeight: "700",
    letterSpacing: 0,
    lineHeight: 17,
    marginTop: 8,
  },
  ideaItem: {
    backgroundColor: "#172033",
    borderLeftColor: "#F59E0B",
    borderLeftWidth: 3,
    borderRadius: 8,
    marginTop: 9,
    paddingHorizontal: 11,
    paddingVertical: 10,
  },
  ideaText: {
    color: "#DDE6F0",
    fontSize: 12,
    fontWeight: "700",
    letterSpacing: 0,
    lineHeight: 17,
  },
  suggestionTitleAlt: {
    color: "#111827",
    fontSize: 14,
    fontWeight: "900",
    letterSpacing: 0,
    marginBottom: 8,
    marginTop: 16,
  },
  mobileIdeaItem: {
    backgroundColor: "#F8FAFC",
    borderColor: "#E2E8F0",
    borderRadius: 8,
    borderWidth: 1,
    marginTop: 8,
    paddingHorizontal: 12,
    paddingVertical: 10,
  },
  mobileIdeaText: {
    color: "#273142",
    fontSize: 13,
    fontWeight: "700",
    letterSpacing: 0,
    lineHeight: 18,
  },
});
