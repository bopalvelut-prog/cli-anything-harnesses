import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['logstash', '-f', '/etc/logstash/conf.d/'])
@cli.command()
def test(): subprocess.run(['logstash', '-t', '-f', '/etc/logstash/conf.d/'])
@cli.command()
def version(): subprocess.run(['logstash', '--version'])
if __name__ == '__main__': cli()
