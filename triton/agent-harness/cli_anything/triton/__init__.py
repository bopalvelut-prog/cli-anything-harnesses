import click
@click.group()
def cli(): pass
@cli.command()
def serve(): click.echo('Triton serve')
@cli.command()
def models(): click.echo('Triton models')
if __name__ == '__main__': cli()
