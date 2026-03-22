import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['fluentd', '-c', '/etc/fluent/fluent.conf'])
@cli.command()
def status(): click.echo('Fluentd running')
@cli.command()
def test(): subprocess.run(['fluentd', '--dry-run', '-c', '/etc/fluent/fluent.conf'])
if __name__ == '__main__': cli()
