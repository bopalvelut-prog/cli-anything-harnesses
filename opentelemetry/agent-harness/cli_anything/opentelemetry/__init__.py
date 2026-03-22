import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['otelcol-contrib', '--config', '/etc/otelcol/config.yaml'])
@cli.command()
def validate(): subprocess.run(['otelcol-contrib', 'validate', '--config', '/etc/otelcol/config.yaml'])
if __name__ == '__main__': cli()
