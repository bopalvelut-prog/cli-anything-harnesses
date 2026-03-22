import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['jaeger-all-in-one'])
@cli.command()
def status(): click.echo('Jaeger running on :16686')
if __name__ == '__main__': cli()
