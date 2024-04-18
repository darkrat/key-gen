{{- define "key-generator.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name -}}
{{- end -}}

{{- define "key-generator.name" -}}
{{- default "key-generator" .Chart.Name -}}
{{- end -}}