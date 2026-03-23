import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_diskencryption running')
@cli.command()
def start(): click.echo('azure_diskencryption started')
if __name__ == '__main__': cli()
