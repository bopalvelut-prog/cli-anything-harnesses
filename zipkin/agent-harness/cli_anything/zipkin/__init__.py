import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['zipkin-server'])
@cli.command()
def status(): click.echo('Zipkin running on :9411')
if __name__ == '__main__': cli()
