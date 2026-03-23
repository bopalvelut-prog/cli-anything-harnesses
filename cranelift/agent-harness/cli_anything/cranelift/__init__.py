import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cranelift running')
@cli.command()
def start(): click.echo('cranelift started')
if __name__ == '__main__': cli()
