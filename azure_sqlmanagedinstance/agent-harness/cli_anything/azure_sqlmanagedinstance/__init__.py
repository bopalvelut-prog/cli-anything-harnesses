import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_sqlmanagedinstance running')
@cli.command()
def start(): click.echo('azure_sqlmanagedinstance started')
if __name__ == '__main__': cli()
