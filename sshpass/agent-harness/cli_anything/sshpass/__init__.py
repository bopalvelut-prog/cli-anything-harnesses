import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sshpass running')
@cli.command()
def start(): click.echo('sshpass started')
if __name__ == '__main__': cli()
