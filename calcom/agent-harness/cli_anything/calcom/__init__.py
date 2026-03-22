import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['cal.com', 'dev'])
@cli.command()
def events(): click.echo('Cal.com events')
if __name__ == '__main__': cli()
