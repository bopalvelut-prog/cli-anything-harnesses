import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_iotsecurity running')
@cli.command()
def start(): click.echo('azure_iotsecurity started')
if __name__ == '__main__': cli()
